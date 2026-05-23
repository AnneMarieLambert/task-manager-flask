import pytest
from src.database import get_db_connection

def test_index_page_empty(client):
    """
    Verifica se a página inicial renderiza corretamente e exibe a mensagem
    de estado vazio padrão quando o banco de dados não possui tarefas.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b'Quadro Kanban' in response.data
    assert b'Sem tarefas pendentes' in response.data
    assert b'Nenhuma em andamento' in response.data

def test_create_task(client, app):
    """
    Valida a inserção bem-sucedida de uma tarefa com título, descrição,
    prioridade e status inicial corretos.
    """
    # Envia requisição POST para criação
    response = client.post('/task/new', data={
        'title': 'Desenhar Diagrama de Caso de Uso',
        'description': 'Modelar no Mermaid para inclusão na documentação',
        'priority': 'Alta',
        'status': 'A Fazer'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Tarefa criada com sucesso!' in response.data
    assert b'Desenhar Diagrama de Caso de Uso' in response.data

    # Verifica se os dados foram salvos corretamente no SQLite
    with app.app_context():
        db = get_db_connection()
        task = db.execute('SELECT * FROM tasks WHERE id = 1').fetchone()
        assert task is not None
        assert task['title'] == 'Desenhar Diagrama de Caso de Uso'
        assert task['description'] == 'Modelar no Mermaid para inclusão na documentação'
        assert task['priority'] == 'Alta'
        assert task['status'] == 'A Fazer'

def test_create_task_validation(client):
    """
    Garante que a aplicação rejeita a criação de tarefas sem título obrigatório.
    """
    response = client.post('/task/new', data={
        'title': '   ',  # Apenas espaços em branco (será stripado)
        'description': 'Teste de validação',
        'priority': 'Média',
        'status': 'A Fazer'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'O t\xc3\xadtulo da tarefa \xc3\xa9 obrigat\xc3\xb3rio!' in response.data  # "O título da tarefa é obrigatório!" em bytes UTF-8

def test_edit_task(client, app):
    """
    Valida a atualização dos dados de uma tarefa existente através do formulário de edição.
    """
    # 1. Cria uma tarefa inicial
    with app.app_context():
        db = get_db_connection()
        db.execute(
            'INSERT INTO tasks (title, description, priority, status) VALUES (?, ?, ?, ?)',
            ('Tarefa Antiga', 'Desc antiga', 'Baixa', 'A Fazer')
        )
        db.commit()

    # 2. Envia modificações via POST
    response = client.post('/task/edit/1', data={
        'title': 'Tarefa Atualizada',
        'description': 'Nova descrição detalhada',
        'priority': 'Alta',
        'status': 'Em Progresso'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Tarefa atualizada com sucesso!' in response.data
    assert b'Tarefa Atualizada' in response.data

    # 3. Verifica alteração no banco
    with app.app_context():
        db = get_db_connection()
        task = db.execute('SELECT * FROM tasks WHERE id = 1').fetchone()
        assert task['title'] == 'Tarefa Atualizada'
        assert task['priority'] == 'Alta'
        assert task['status'] == 'Em Progresso'

def test_delete_task(client, app):
    """
    Verifica se a tarefa é removida corretamente do banco de dados ao ser excluída.
    """
    # 1. Insere tarefa para teste
    with app.app_context():
        db = get_db_connection()
        db.execute(
            'INSERT INTO tasks (title, description, priority, status) VALUES (?, ?, ?, ?)',
            ('Tarefa para Excluir', 'Será deletada', 'Média', 'A Fazer')
        )
        db.commit()

    # 2. Executa a deleção
    response = client.post('/task/delete/1', follow_redirects=True)
    assert response.status_code == 200
    assert b'Tarefa exclu\xc3\xadda com sucesso!' in response.data # "Tarefa excluída com sucesso!"

    # 3. Garante que ela não existe mais
    with app.app_context():
        db = get_db_connection()
        task = db.execute('SELECT * FROM tasks WHERE id = 1').fetchone()
        assert task is None

def test_toggle_task_status(client, app):
    """
    Valida a alternância de status rápida de pendente ('A Fazer') para 'Concluído'
    e vice-versa ao disparar a rota toggle.
    """
    # 1. Insere tarefa 'A Fazer'
    with app.app_context():
        db = get_db_connection()
        db.execute(
            'INSERT INTO tasks (title, description, priority, status) VALUES (?, ?, ?, ?)',
            ('Alternar Status', 'Descrição do teste', 'Baixa', 'A Fazer')
        )
        db.commit()

    # 2. Primeiro clique: Muda para Concluído
    response = client.post('/task/toggle/1', follow_redirects=True)
    assert response.status_code == 200
    

    with app.app_context():
        db = get_db_connection()
        task = db.execute('SELECT * FROM tasks WHERE id = 1').fetchone()
        assert task['status'] == 'Concluído'

    # 3. Segundo clique: Retorna para A Fazer
    response = client.post('/task/toggle/1', follow_redirects=True)
    assert response.status_code == 200
    

    with app.app_context():
        db = get_db_connection()
        task = db.execute('SELECT * FROM tasks WHERE id = 1').fetchone()
        assert task['status'] == 'A Fazer'
