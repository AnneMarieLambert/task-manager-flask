-- Script SQL para inicialização do Banco de Dados SQLite
-- Define a estrutura da tabela principal de tarefas (tasks)

DROP TABLE IF EXISTS tasks;

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    priority TEXT NOT NULL CHECK(priority IN ('Alta', 'Média', 'Baixa')) DEFAULT 'Média',
    status TEXT NOT NULL CHECK(status IN ('A Fazer', 'Em Progresso', 'Concluído')) DEFAULT 'A Fazer',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Trigger para atualizar automaticamente o campo updated_at quando uma tarefa for modificada
CREATE TRIGGER update_tasks_timestamp AFTER UPDATE ON tasks
BEGIN
    UPDATE tasks SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;
