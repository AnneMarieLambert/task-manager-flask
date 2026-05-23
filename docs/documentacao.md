# Documentação Técnica do Projeto (Engenharia de Software)

Este documento reúne a fundamentação teórica de Engenharia de Software aplicada no desenvolvimento do sistema **KanbanTasker**, detalhando a especificação de requisitos, a arquitetura do software e as decisões de engenharia ágil adotadas.

---

## 1. Especificação de Requisitos

O desenvolvimento do sistema foi orientado pelo levantamento de requisitos funcionais (o que o sistema deve fazer) e não-funcionais (como o sistema deve operar).

### Requisitos Funcionais (RF)
*   **RF-001 — Cadastro de Tarefas**: O sistema deve permitir a inclusão de uma tarefa, contendo obrigatoriamente um título, além de descrição opcional, nível de prioridade e status inicial.
*   **RF-002 — Listagem Kanban**: O sistema deve listar as tarefas de forma visual em três colunas baseadas em seu status: "A Fazer", "Em Progresso" e "Concluído".
*   **RF-003 — Edição de Tarefas**: O sistema deve permitir a alteração das informações cadastrais (título, descrição, prioridade e status) de qualquer tarefa ativa.
*   **RF-004 — Exclusão Física**: O sistema deve permitir a deleção permanente de uma tarefa por meio de confirmação do usuário.
*   **RF-005 — Conclusão Rápida (Toggle)**: O sistema deve fornecer um atalho rápido na tela para alternar o status da tarefa entre pendente e concluída.
*   **RF-006 — Classificação de Prioridades**: O sistema deve expor visualmente o nível de criticidade da tarefa (Alta, Média, Baixa) no card do Kanban através de cores correspondentes.

### Requisitos Não-Funcionais (RNF)
*   **RNF-001 — Arquitetura Leve**: O sistema deve rodar sem a necessidade de servidores pesados de banco de dados, utilizando SQLite (arquivo local).
*   **RNF-002 — Portabilidade e Testabilidade**: O sistema deve ser testado automaticamente de maneira isolada em qualquer ambiente através do framework Pytest.
*   **RNF-003 — Responsividade Visual**: A interface do usuário deve se adaptar de maneira fluida a telas de smartphones, tablets e desktops utilizando CSS Flexbox e Grid.
*   **RNF-004 — Prevenção de Injeções**: Todas as consultas ao banco de dados devem utilizar queries SQL parametrizadas, mitigando ataques de injeção de código (SQL Injection).

---

## 2. Arquitetura de Software

O KanbanTasker segue o padrão de arquitetura **MVC (Model-View-Controller)** adaptado para o ecossistema Flask:

```text
                  +--------------------------------+
                  |            USUÁRIO             |
                  +--------------------------------+
                                  |
                   Requisições    |    Renderização
                   HTTP (GET/POST)|    de HTML/CSS
                                  v
                  +--------------------------------+
                  |         VIEW/TEMPLATES         |  <--- (Flask Jinja2)
                  +--------------------------------+
                                  |
                       Desvia     |    Interage
                       Ações      |    e Atualiza
                                  v
                  +--------------------------------+
                  |      CONTROLLER (app.py)       |  <--- (Rotas Flask)
                  +--------------------------------+
                                  |
                       Consulta   |    Retorna
                       e Salva    |    Dados
                                  v
                  +--------------------------------+
                  |      MODEL (database.py)       |  <--- (Queries SQLite)
                  +--------------------------------+
                                  |
                     Operações    |    Retorna
                     de Disco     |    Registros
                                  v
                  +--------------------------------+
                  |     PERSISTÊNCIA (SQLite)      |  <--- (tasks.db)
                  +--------------------------------+
```

*   **Model (`src/database.py`)**: Gerencia o estado e a persistência dos dados diretamente no arquivo SQLite. Contém as queries de baixo nível.
*   **View (`/templates`, `/static`)**: Renderiza a interface dinâmica por meio de templates Jinja2. Estilizado com CSS purista e moderno.
*   **Controller (`src/app.py`)**: Orquestra a lógica de controle, lida com formulários HTTP, define regras de negócio de validação e direciona o fluxo de telas.

---

## 3. Gestão e Decisões de Metodologia Ágil (Kanban)

A equipe optou pelo framework ágil **Kanban** em substituição ao Scrum rígido por se alinhar melhor ao desenvolvimento contínuo de projetos de menor porte:

1.  **Limitação de Trabalho em Progresso (WIP - Work in Progress)**:
    *   Para evitar gargalos, a equipe estabeleceu que a coluna "Em Progresso" possui um limite de cards ativos simultâneos. Isso otimiza o fluxo de entrega (Lead Time).
2.  **Quadro Físico e Digital**:
    *   O quadro Kanban reproduzido no front-end do sistema reflete diretamente o fluxo operacional real utilizado pela equipe de engenharia durante o desenvolvimento desta disciplina acadêmica.
3.  **Priorização Clara**:
    *   A priorização de tarefas em Alta, Média e Baixa (adicionada durante a mudança de escopo) permitiu resolver problemas de "paralisia de análise", garantindo que tarefas críticas (como testes automatizados e estrutura do banco) fossem entregues antes de perfumarias de interface.
