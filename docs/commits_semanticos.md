## 1. O que são Commits Semânticos?
Commits semânticos são mensagens de commit estruturadas de forma padronizada para indicar claramente o *propósito* da alteração efetuada no código. O padrão básico utilizado é:
`tipo(escopo): descrição sucinta`

Os principais tipos utilizados são:
*   `feat`: Introdução de uma nova funcionalidade (Feature).
*   `fix`: Correção de um bug.
*   `docs`: Alterações exclusivamente em arquivos de documentação.
*   `style`: Alterações estéticas que não afetam o comportamento do código (CSS, formatação).
*   `test`: Adição ou modificação de arquivos de teste.
*   `chore`: Alterações administrativas ou de configuração (ex: `.gitignore`, `requirements.txt`).

---

## 2. Linha do Tempo: 10 Commits Sugeridos para o Projeto

### Commit #01 — Estrutura Inicial e Dependências
*   **Mensagem**: `chore: inicializar estrutura de pastas e arquivo de dependencias`
*   **Descrição**: Configuração básica do projeto, incluindo os diretórios solicitados (`/src`, `/templates`, `/static`, `/tests`, `/docs`), criação do arquivo `requirements.txt` e configuração do `.gitignore` inicial.

### Commit #02 — Esquema do Banco SQLite
*   **Mensagem**: `feat(db): criar schema sql e triggers de atualizacao automatica`
*   **Descrição**: Implementação do arquivo `src/schema.sql` definindo a estrutura da tabela `tasks` e a trigger SQLite para atualização do timestamp `updated_at`.

### Commit #03 — Conexão com o Banco de Dados
*   **Mensagem**: `feat(db): codificar conexao sqlite e funcoes CRUD`
*   **Descrição**: Implementação do arquivo `src/database.py` contendo as funções utilitárias de conexão por contexto do Flask (`get_db_connection()`), inicialização (`init_db()`) e as queries do CRUD de tarefas.

### Commit #04 — Rotas Flask e Fábrica de App
*   **Mensagem**: `feat(app): configurar factory create_app e mapear rotas basicas`
*   **Descrição**: Criação do arquivo `src/app.py` com o padrão Application Factory do Flask e definição inicial das rotas do CRUD de tarefas.

### Commit #05 — Layout de Base HTML
*   **Mensagem**: `docs(view): estruturar template base html com suporte a flash alerts`
*   **Descrição**: Criação do arquivo `templates/base.html` contendo a marcação padrão de cabeçalho, navegação, rodapé acadêmico e container para mensagens flash.

### Commit #06 — Painel Kanban e Estilos Visuais
*   **Mensagem**: `style(ui): aplicar layout kanban moderno e css glassmorphism`
*   **Descrição**: Criação do arquivo `static/css/style.css` com a estilização dark mode e glassmorphism premium do quadro Kanban e inserção do template `templates/index.html`.

### Commit #07 — Telas de Formulários CRUD
*   **Mensagem**: `feat(view): codificar telas de criacao e edicao de tarefas`
*   **Descrição**: Criação dos templates HTML `templates/create.html` e `templates/edit.html` com suporte completo a validações de campos obrigatórios e estilos harmoniosos.

### Commit #08 — Mudança de Escopo: Campo de Prioridades
*   **Mensagem**: `feat(scope): adicionar funcionalidade de prioridade das tarefas`
*   **Descrição**: Alteração da tabela no SQLite (`CHECK` constraint), atualização dos formulários HTML para inclusão do campo Prioridade (Alta, Média, Baixa) e renderização de badges coloridos correspondentes.

### Commit #09 — Suíte de Testes com Pytest
*   **Mensagem**: `test: programar testes automatizados do CRUD e fixtures`
*   **Descrição**: Implementação de `tests/conftest.py` com banco em memória isolado para testes e escrita de testes funcionais em `tests/test_tasks.py` para as ações do CRUD.

### Commit #10 — Integração Contínua (CI)
*   **Mensagem**: `chore(ci): configurar workflow do github actions para testes automatizados`
*   **Descrição**: Criação do pipeline de CI no arquivo `.github/workflows/tests.yml` para validar pull requests e pushes na branch principal de forma automatizada no GitHub.
