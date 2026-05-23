import os
from flask import Flask, render_template, request, redirect, url_for, flash
from src.database import (
    close_db_connection, init_db, get_all_tasks, get_task_by_id,
    create_task, update_task, delete_task, toggle_task_status
)

def create_app(test_config=None):
    """
    Função de fábrica do Flask (Application Factory).
    Configura e inicializa a aplicação Flask, definindo os caminhos corretos de
    templates e arquivos estáticos localizados fora do subdiretório 'src/'.
    """
    # Como 'app.py' está localizado dentro de '/src', configuramos explicitamente
    # a pasta de templates e arquivos estáticos no nível da raiz do projeto.
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates'),
        static_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static')
    )
    
    # Configurações padrão do sistema
    app.config.from_mapping(
        SECRET_KEY='engenharia-de-software-super-secreta',
        DATABASE=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'instance', 'tasks.db'),
    )
    
    # Se houver configuração de teste (ex: injetada pelo Pytest), ela sobrescreve o padrão
    if test_config is not None:
        app.config.from_mapping(test_config)
        
    # Garante que o diretório da instância (onde o SQLite reside) seja criado
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
        
    # Registra o encerramento do banco de dados na desmontagem da requisição Flask
    app.teardown_appcontext(close_db_connection)
    
    # --- ROTAS DA APLICAÇÃO ---
    
    @app.route('/')
    def index():
        """
        Página principal: Dashboard da Metodologia Ágil (Quadro Kanban).
        Recupera as tarefas do SQLite e as agrupa em colunas baseadas em seus status.
        """
        tasks = get_all_tasks()
        
        # Estrutura do Kanban com 3 colunas padrão
        kanban = {
            'A Fazer': [],
            'Em Progresso': [],
            'Concluído': []
        }
        
        # Organiza as tarefas em suas respectivas colunas
        for task in tasks:
            status = task['status']
            if status in kanban:
                kanban[status].append(task)
            else:
                kanban['A Fazer'].append(task)
                
        return render_template('index.html', kanban=kanban, tasks=tasks)
        
    @app.route('/task/new', methods=('GET', 'POST'))
    def create():
        """
        Funcionalidade: Criar nova tarefa.
        Valida os dados de entrada e insere o registro no banco.
        """
        if request.method == 'POST':
            title = request.form['title'].strip()
            description = request.form['description'].strip()
            priority = request.form['priority']
            status = request.form['status']
            
            error = None
            # Validação básica de regras de negócio
            if not title:
                error = 'O título da tarefa é obrigatório!'
            elif priority not in ('Alta', 'Média', 'Baixa'):
                error = 'Prioridade selecionada é inválida!'
            elif status not in ('A Fazer', 'Em Progresso', 'Concluído'):
                error = 'Status selecionado é inválida!'
                
            if error is None:
                create_task(title, description, priority, status)
                flash('Tarefa criada com sucesso!', 'success')
                return redirect(url_for('index'))
                
            flash(error, 'danger')
            
        return render_template('create.html')
        
    @app.route('/task/edit/<int:id>', methods=('GET', 'POST'))
    def edit(id):
        """
        Funcionalidade: Editar tarefa existente.
        Busca a tarefa pelo ID e processa as atualizações do formulário.
        """
        task = get_task_by_id(id)
        if task is None:
            flash(f'Tarefa #{id} não encontrada!', 'warning')
            return redirect(url_for('index'))
            
        if request.method == 'POST':
            title = request.form['title'].strip()
            description = request.form['description'].strip()
            priority = request.form['priority']
            status = request.form['status']
            
            error = None
            if not title:
                error = 'O título da tarefa é obrigatório!'
            elif priority not in ('Alta', 'Média', 'Baixa'):
                error = 'Prioridade selecionada é inválida!'
            elif status not in ('A Fazer', 'Em Progresso', 'Concluído'):
                error = 'Status selecionado é inválido!'
                
            if error is None:
                update_task(id, title, description, priority, status)
                flash('Tarefa atualizada com sucesso!', 'success')
                return redirect(url_for('index'))
                
            flash(error, 'danger')
            
        return render_template('edit.html', task=task)
        
    @app.route('/task/delete/<int:id>', methods=('POST',))
    def delete(id):
        """
        Funcionalidade: Excluir tarefa.
        Remove permanentemente o registro de tarefa correspondente ao ID.
        """
        task = get_task_by_id(id)
        if task is None:
            flash(f'Tarefa #{id} não encontrada!', 'warning')
        else:
            delete_task(id)
            flash('Tarefa excluída com sucesso!', 'success')
        return redirect(url_for('index'))
        
    @app.route('/task/toggle/<int:id>', methods=('POST',))
    def toggle(id):
        """
        Funcionalidade rápida: Mudar status da tarefa.
        Alterna rapidamente entre os estados (útil para marcar e desmarcar como concluída).
        """
        task = get_task_by_id(id)
        if task is None:
            flash(f'Tarefa #{id} não encontrada!', 'warning')
        else:
            new_status = toggle_task_status(id)
            flash(f'Tarefa atualizada para o status: "{new_status}"!', 'info')
        return redirect(url_for('index'))
        
    return app

if __name__ == '__main__':
    # Ponto de entrada para execução local
    app = create_app()
    
    # Inicializa o banco de dados caso não exista o arquivo .db
    db_path = app.config['DATABASE']
    if not os.path.exists(db_path):
        print("Banco de dados não encontrado localmente. Inicializando banco...")
        init_db(app)
        print("Banco de dados inicializado com sucesso!")
        
    # Inicializa o servidor local com o modo Debug habilitado
    app.run(debug=True, host='127.0.0.1', port=5000)
