import sqlite3
import os
from flask import g, current_app

# Caminho padrão para o banco de dados no diretório 'instance' da aplicação
DATABASE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'instance', 'tasks.db')

def get_db_connection():
    """
    Estabelece ou recupera a conexão com o banco de dados SQLite.
    Utiliza o contexto global 'g' do Flask para garantir que a mesma conexão
    seja reaproveitada durante uma mesma requisição web.
    """
    if 'db' not in g:
        # Recupera o caminho configurado (útil nos testes para usar banco em memória ou temporário)
        db_path = current_app.config.get('DATABASE', DATABASE_PATH)
        
        # Cria a pasta 'instance' caso ela ainda não exista
        db_dir = os.path.dirname(db_path)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir, exist_ok=True)
            
        g.db = sqlite3.connect(db_path)
        # Habilita o acesso aos dados por nome de coluna (dict-like)
        g.db.row_factory = sqlite3.Row
        
    return g.db

def close_db_connection(e=None):
    """
    Fecha a conexão do banco de dados ao encerrar o contexto da requisição Flask.
    """
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db(app):
    """
    Inicializa o banco de dados executando as instruções do arquivo schema.sql.
    Deve ser chamado com o contexto do aplicativo Flask ativo.
    """
    with app.app_context():
        db = get_db_connection()
        schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
        with open(schema_path, 'r', encoding='utf-8') as f:
            db.executescript(f.read())
        db.commit()

# --- OPERAÇÕES DO CRUD (Camada de persistência de dados) ---

def get_all_tasks():
    """
    Retorna todas as tarefas registradas no banco de dados, ordenadas por data de criação (mais recentes primeiro).
    """
    db = get_db_connection()
    return db.execute('SELECT * FROM tasks ORDER BY created_at DESC').fetchall()

def get_task_by_id(task_id):
    """
    Busca e retorna uma única tarefa pelo seu ID único. Retorna None se não for encontrada.
    """
    db = get_db_connection()
    return db.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()

def create_task(title, description, priority, status='A Fazer'):
    """
    Insere uma nova tarefa no banco de dados.
    """
    db = get_db_connection()
    db.execute(
        'INSERT INTO tasks (title, description, priority, status) VALUES (?, ?, ?, ?)',
        (title, description, priority, status)
    )
    db.commit()

def update_task(task_id, title, description, priority, status):
    """
    Atualiza as informações de uma tarefa existente no banco de dados.
    """
    db = get_db_connection()
    db.execute(
        'UPDATE tasks SET title = ?, description = ?, priority = ?, status = ? WHERE id = ?',
        (title, description, priority, status, task_id)
    )
    db.commit()

def delete_task(task_id):
    """
    Exclui permanentemente uma tarefa do banco de dados utilizando seu ID.
    """
    db = get_db_connection()
    db.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    db.commit()

def toggle_task_status(task_id):
    """
    Altera o status de uma tarefa rapidamente.
    Se estiver marcada como 'Concluído', altera para 'A Fazer'.
    Se estiver em qualquer outro status, altera para 'Concluído'.
    """
    db = get_db_connection()
    task = get_task_by_id(task_id)
    if task:
        new_status = 'A Fazer' if task['status'] == 'Concluído' else 'Concluído'
        db.execute('UPDATE tasks SET status = ? WHERE id = ?', (new_status, task_id))
        db.commit()
        return new_status
    return None
