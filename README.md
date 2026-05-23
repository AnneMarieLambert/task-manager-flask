# KanbanTasker - Sistema de Gerenciamento de Tarefas Ágil

Este projeto é um sistema web acadêmico de gerenciamento de tarefas estruturado sob a ótica das disciplinas de **Engenharia de Software** e **Metodologias Ágeis**. A aplicação foi desenvolvida utilizando a linguagem **Python** com o framework micro **Flask**, persistência de dados local leve com **SQLite** nativo e uma suíte completa de testes automatizados com **Pytest**, integrada a um pipeline de CI via **GitHub Actions**.

---

##  Objetivo do Projeto
O objetivo do KanbanTasker é prover uma ferramenta simples, didática e de alta qualidade visual para simular o ciclo de vida de tarefas em um fluxo ágil de desenvolvimento. Ele serve como entrega acadêmica modelo, demonstrando boas práticas de modularização de código, design limpo, cobertura de testes funcionais e conceitos práticos de gerenciamento ágil.

---

##  Tecnologias Utilizadas
*   **Linguagem**: Python (versão >= 3.10)
*   **Framework Web**: Flask (padrão Application Factory)
*   **Banco de Dados**: SQLite3 (nativo do Python, sem ORMs para fins de clareza didática)
*   **Estilização e UI**: HTML5 semântico e CSS3 puro (Design moderno com Glassmorphism e Dark Mode)
*   **Comportamento Client-Side**: Javascript moderno (Vanilla JS para micro-interações)
*   **Framework de Testes**: Pytest
*   **Integração Contínua (CI)**: GitHub Actions
*   **Documentação UML**: Mermaid Diagramming Tool

---

##  Estrutura Organizacional do Projeto
O projeto foi estruturado seguindo os padrões profissionais da Engenharia de Software, organizando as responsabilidades de forma clara e limpa:

```text
task-manager-flask/
├── .github/
│   └── workflows/
│       └── tests.yml            # Configuração do Pipeline CI (GitHub Actions)
├── docs/
│   ├── diagrama_classes.md      # Diagrama de Classes UML em formato Mermaid
│   ├── diagrama_casos_uso.md    # Diagrama de Casos de Uso UML em formato Mermaid
│   ├── kanban_cards.md          # Cards Kanban da Sprint do Projeto
│   ├── commits_semanticos.md    # Guia com os 10 commits semânticos sugeridos
│   └── documentacao.md          # Requisitos de Software, Arquitetura e Decisões
├── src/
│   ├── __init__.py              # Declaração de pacote Python
│   ├── app.py                   # Inicialização do Flask (Factory) e Rotas Controller
│   ├── database.py              # Camada de Persistência (Model/CRUD SQLite)
│   └── schema.sql               # Estrutura inicial das tabelas SQL
├── static/
│   ├── css/
│   │   └── style.css            # Estilização premium (Cores, Fontes e Efeitos)
│   └── js/
│       └── main.js              # Comportamentos de confirmação e alertas
├── templates/
│   ├── base.html                # Layout mestre HTML (Nav, Footer, Flask Flash)
│   ├── index.html               # Tela do Painel Kanban e cards das colunas
│   ├── create.html              # Tela de formulário de cadastro de tarefas
│   └── edit.html                # Tela de formulário de atualização de tarefas
├── tests/
│   ├── __init__.py              # Declaração de pacote de testes
│   ├── conftest.py              # Configuração de Fixtures do Pytest (Banco temporário)
│   └── test_tasks.py            # Testes do CRUD e Validação
├── .gitignore                   # Arquivos ignorados pelo controle de versão Git
├── README.md                    # Este documento explicativo
└── requirements.txt             # Dependências e bibliotecas externas do projeto
```

---

##  Metodologia Ágil Utilizada (Kanban)
O sistema foi projetado especificamente para espelhar a metodologia ágil **Kanban**, amplamente adotada em equipes de desenvolvimento modernas devido à sua flexibilidade. 

O quadro visual é dividido nas três colunas essenciais:
1.  **A Fazer (To Do)**: Itens do backlog priorizados e aguardando execução.
2.  **Em Progresso (Doing)**: Atividades em desenvolvimento ativo por membros do time.
3.  **Concluído (Done)**: Tarefas que passaram pelos critérios de aceitação e estão prontas (Definition of Ready / Done).

A equipe simulou o backlog de desenvolvimento do próprio projeto sob a forma de cards de Histórias de Usuários (User Stories) completos. A sugestão prática desses cards encontra-se detalhada no arquivo [docs/kanban_cards.md](file:///C:/Users/user/.gemini/antigravity/scratch/task-manager-flask/docs/kanban_cards.md).

---

##  Mudança de Escopo: Prioridade das Tarefas
Durante as reuniões de planejamento ágil no decorrer do ciclo de desenvolvimento, a equipe identificou a necessidade crítica de sinalizar a criticidade de cada atividade diretamente no quadro visual para que os desenvolvedores pudessem focar primeiro em tarefas bloqueantes ou urgentes.

Dessa forma, foi aprovada uma **Mudança de Escopo oficial** para incorporar a funcionalidade de **Prioridade das Tarefas**:
*   Cada tarefa agora possui obrigatoriamente um nível classificado em: **Alta**, **Média** ou **Baixa**.
*   Formulários de criação e edição foram alterados para expor e receber essa nova métrica.
*   Cards no Kanban ganharam badges coloridos dinâmicos e uma borda indicativa (Vermelho para prioridade Alta, Amarelo para Média e Verde para Baixa), aumentando a eficácia visual do quadro.

---

##  Explicação do Sistema (Como Funciona)
A aplicação funciona como um sistema completo de gerenciamento de tarefas (CRUD):
*   **Criar Tarefa**: Permite registrar título, descrição rica, prioridade e coluna inicial.
*   **Listar Tarefas**: O dashboard divide as tarefas criadas dinamicamente entre as 3 colunas ágeis.
*   **Editar Tarefa**: Altera os dados de qualquer tarefa a qualquer momento.
*   **Marcar como Concluída**: Um atalho rápido na base do card alterna instantaneamente o status entre pendente e concluída, movendo o card entre as colunas sem necessidade de abrir formulários complexos.
*   **Excluir Tarefa**: Remove permanentemente a tarefa do SQLite. Inclui uma proteção contra exclusões acidentais via confirmação Javascript na interface.

---

##  Como Executar o Projeto Localmente

### Pré-requisitos
*   Python 3.10 ou superior instalado em seu sistema operacional.

### Passo a Passo de Execução

1.  **Acessar a pasta raiz do projeto**:
    ```bash
    cd task-manager-flask
    ```

2.  **Criar o ambiente virtual (venv)**:
    ```bash
    python -m venv .venv
    ```

3.  **Ativar o ambiente virtual**:
    *   **No Windows**:
        ```bash
        .venv\Scripts\activate
        ```
    *   **No Linux/macOS**:
        ```bash
        source .venv/bin/activate
        ```

4.  **Instalar as dependências do projeto**:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Executar o servidor de desenvolvimento**:
    ```bash
    python src/app.py
    ```

6.  **Acessar a aplicação**:
    Abra seu navegador web e digite: [http://127.0.0.1:5000](http://127.0.0.1:5000). O banco de dados SQLite será inicializado automaticamente na primeira inicialização (criando o arquivo `instance/tasks.db`).

---

##  Como Executar os Testes Automatizados
Os testes foram estruturados de forma isolada usando **Pytest** e utilizam um banco de dados físico temporário em disco que é destruído logo após a finalização da execução, não alterando seus dados locais reais.

Para rodar os testes, garanta que seu ambiente virtual esteja ativo e execute:
```bash
pytest -v
```

Isso rodará toda a suíte de testes de rotas, CRUD e validações de dados presentes no arquivo [tests/test_tasks.py](file:///C:/Users/user/.gemini/antigravity/scratch/task-manager-flask/tests/test_tasks.py), detalhando a aprovação de cada cenário.

---

##  Integração Contínua (GitHub Actions)
Este projeto conta com um fluxo de **Integração Contínua (CI)** totalmente configurado no arquivo [tests.yml](file:///C:/Users/user/.gemini/antigravity/scratch/task-manager-flask/.github/workflows/tests.yml).

Sempre que a equipe submete um novo commit ou abre uma solicitação de mesclagem (Pull Request) nas branches de produção (`main`/`master`), os servidores do GitHub realizam de forma 100% autônoma as seguintes etapas:
1.  Fazem o checkout do código do repositório.
2.  Preparam uma máquina Linux limpa com a versão 3.11 do Python.
3.  Instalam as dependências declaradas no `requirements.txt`.
4.  Roda a suíte de testes automatizados com o `pytest`.

Se algum teste falhar, o GitHub avisa os membros da equipe e o administrador do repositório pode impedir a união do código quebrado na branch estável, garantindo a **qualidade do software** e o conceito de **entrega contínua (CD)** de software.
