# Quadro de Histórias de Usuário & Cards Kanban (Sprint Backlog)

Este documento simula a distribuição de tarefas no quadro ágil da equipe de desenvolvimento do projeto **KanbanTasker**, servindo como documentação prática de Metodologia Ágil solicitada na disciplina de Engenharia de Software.

---

## 📋 Coluna: A Fazer (Backlog Selecionado para a Sprint)

### Card US05 - Integração Contínua com GitHub Actions
*   **ID da Tarefa**: `#TSK-005`
*   **Título**: Configurar Pipeline de CI
*   **Prioridade**: 🟢 Baixa
*   **Story Points**: 3 SPs
*   **Descrição**: Criar um arquivo YAML na pasta `.github/workflows` que execute automaticamente o comando `pytest` sempre que houver `push` ou `pull_request` no branch `main`.
*   **Critérios de Aceite**:
    *   Pipeline dispara no GitHub Actions de forma automatizada.
    *   Falhas nos testes impedem o merge.
    *   Instalação das dependências é feita de forma limpa.

### Card US06 - Elaboração da Documentação do Projeto
*   **ID da Tarefa**: `#TSK-006`
*   **Título**: Desenhar Diagramas UML e Escrever README
*   **Prioridade**: 🟡 Média
*   **Story Points**: 5 SPs
*   **Descrição**: Redigir o arquivo de documentação técnica do sistema, desenhar os diagramas de caso de uso e classes utilizando sintaxe Mermaid e criar a lista de commits recomendados.
*   **Critérios de Aceite**:
    *   README completo com instruções claras de execução e teste.
    *   Diagramas renderizando perfeitamente no visualizador do GitHub.

---

## 🚀 Coluna: Em Progresso (Tarefas Ativas)

### Card US03 - Testes Automatizados de Unidade e Integração
*   **ID da Tarefa**: `#TSK-003`
*   **Título**: Desenvolver Suíte de Testes com Pytest
*   **Prioridade**: 🔴 Alta
*   **Story Points**: 8 SPs
*   **Descrição**: Escrever testes para as rotas do Flask de criação, listagem, edição, deleção e validação do banco de dados SQLite.
*   **Critérios de Aceite**:
    *   Mínimo de 5 casos de teste.
    *   Utilizar fixtures do Pytest para criar banco de dados isolado em memória.
    *   100% dos testes devem passar localmente.

---

## 🎯 Coluna: Concluído (Definição de Pronto - DoD)

### Card US01 - Configuração Inicial da Aplicação Web
*   **ID da Tarefa**: `#TSK-001`
*   **Título**: Inicializar Flask Factory e SQLite
*   **Prioridade**: 🔴 Alta
*   **Story Points**: 5 SPs
*   **Descrição**: Montar o esqueleto do projeto contendo a estrutura de pastas correta e criar o arquivo `app.py` utilizando o padrão de fábrica `create_app()`. Criar arquivo `schema.sql` com as tabelas de tarefas e triggers.
*   **Critérios de Aceite**:
    *   Estrutura de pastas `/src`, `/templates`, `/static`, `/tests` criada.
    *   Execução do script cria a pasta `instance` e o arquivo do banco `.db`.

### Card US02 - CRUD Completo de Tarefas
*   **ID da Tarefa**: `#TSK-002`
*   **Título**: Implementar Rotas CRUD e Front-End do Kanban
*   **Prioridade**: 🔴 Alta
*   **Story Points**: 13 SPs
*   **Descrição**: Implementar as rotas Flask para cadastrar tarefas, editar informações, excluir permanentemente e mudar status. Criar a interface visual responsiva e moderna em HTML e CSS simulando um quadro Kanban de três colunas.
*   **Critérios de Aceite**:
    *   CRUD funciona de ponta a ponta sem quebras.
    *   Layout responsivo no celular e desktop.
    *   Interface com estilo de Glassmorphism e Dark Mode premium.

### Card US04 - Mudança de Escopo: Priorização de Tarefas (Feature Adicional)
*   **ID da Tarefa**: `#TSK-004`
*   **Título**: Adicionar campo "Prioridade" às tarefas
*   **Prioridade**: 🟡 Média
*   **Story Points**: 3 SPs
*   **Descrição**: Alterar o banco de dados e formulários para permitir classificar as tarefas em níveis: Alta, Média e Baixa. Exibir badges coloridos correspondentes em cada card no painel do Kanban.
*   **Critérios de Aceite**:
    *   Banco SQLite aceita apenas valores ('Alta', 'Média', 'Baixa') por meio de uma restrição `CHECK`.
    *   Badges mudam de cor conforme a prioridade (Vermelho para Alta, Amarelo para Média, Verde para Baixa).
