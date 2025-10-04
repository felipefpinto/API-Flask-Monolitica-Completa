# API Flask - Monolítica Completa

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1.2-black?style=for-the-badge&logo=flask)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.43-orange?style=for-the-badge&logo=sqlalchemy)
![SQLite](https://img.shields.io/badge/SQLite-database-0769AD?style=for-the-badge&logo=sqlite)
![Flasgger](https://img.shields.io/badge/Flasgger-0.9.7.1-purple?style=for-the-badge)

## Descrição

Este projeto é uma API RESTful monolítica completa desenvolvida com Flask, Python e SQLAlchemy. Ele foi projetado para gerenciar informações de uma instituição de ensino, incluindo professores, turmas e alunos. A API oferece endpoints para operações CRUD (Criar, Ler, Atualizar, Deletar) para cada uma dessas entidades, com validações e relacionamentos entre elas.

**Principais Características:**

*   **Gerenciamento de Professores**: Crie, liste, visualize, atualize e exclua professores, incluindo informações como nome, idade, matéria e observações.
*   **Gerenciamento de Turmas**: Crie, liste, visualize, atualize e exclua turmas, associando-as a um professor e definindo seu status (ativo/inativo).
*   **Gerenciamento de Alunos**: Crie, liste, visualize, atualize e exclua alunos, associando-os a uma turma e registrando dados como data de nascimento, notas semestrais e média final. A idade do aluno é calculada automaticamente com base na data de nascimento.
*   **Banco de Dados SQLite**: Utiliza SQLite como banco de dados, ideal para desenvolvimento e prototipagem rápida.
*   **Validação de Chaves Estrangeiras**: Configuração para garantir a integridade referencial no SQLite.
*   **Estrutura Modular**: Organização do código em blueprints para controllers, modelos e helpers, facilitando a manutenção e escalabilidade.
*   **Documentação de API (Flasgger)**: Preparado para integração com Flasgger para geração automática de documentação Swagger/OpenAPI.

## Instalação

Siga os passos abaixo para configurar e executar o projeto localmente.

### Pré-requisitos

*   Python 3.9+
*   `pip` (gerenciador de pacotes do Python)

### Passos para Instalação

1.  **Clone o repositório**:
    ```bash
    git clone https://github.com/seu-usuario/API-Flask-Monolitica-Completa.git
    cd API-Flask-Monolitica-Completa
    ```

2.  **Crie e ative um ambiente virtual (recomendado)**:
    ```bash
    python -m venv venv
    # No Windows
    .\venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```
    As dependências incluem:
    *   `flasgger==0.9.7.1`
    *   `Flask==3.1.2`
    *   `flask_sqlalchemy==3.1.1`
    *   `SQLAlchemy==2.0.43`

4.  **Inicialize o banco de dados**:
    As tabelas do banco de dados serão criadas automaticamente na primeira execução da aplicação, graças ao `db.create_all()` no `app.py`.

## Uso

Para iniciar a aplicação, execute o arquivo `app.py`:

```bash
python app.py
```

A API estará disponível em `http://127.0.0.1:5000` (ou outra porta se configurada).

### Endpoints da API

A API é organizada em torno de três entidades principais: `professores`, `turmas` e `alunos`.

#### Professores (`/professores`)

*   **`POST /professores`**: Cria um novo professor.
    *   **Corpo da Requisição (JSON)**:
        ```json
        {
            "nome": "Nome do Professor",
            "idade": 45,
            "materia": "Matemática",
            "obs": "Professor experiente em cálculo."
        }
        ```
    *   **Resposta**: `{"mensagem": "Professor criado com sucesso!"}` (201)
*   **`GET /professores`**: Lista todos os professores.
    *   **Resposta**: `{"professores": [...], "total_professores": N}` (200)
*   **`GET /professores/<int:id_professor>`**: Retorna os detalhes de um professor específico.
    *   **Resposta**: `{"mensagem": "Professor encontrado com sucesso!", "dados_professor": {...}}` (200) ou `{"mensagem": "Professor não encontrado"}` (404)
*   **`PUT /professores/<int:id_professor>`**: Atualiza os dados de um professor.
    *   **Corpo da Requisição (JSON)**:
        ```json
        {
            "nome": "Novo Nome",
            "materia": "Física"
        }
        ```
    *   **Resposta**: `{"mensagem": "Dados do professor atualizados com sucesso!"}` (200) ou `{"mensagem": "Professor não encontrado"}` (404)
*   **`DELETE /professores/<int:id_professor>`**: Exclui um professor.
    *   **Resposta**: `{"mensagem": "Professor excluído com sucesso"}` (200) ou `{"mensagem": "Professor não encontrado"}` (404)
    *   **Erro**: `{"mensagem": "Não é possível excluir o professor, pois ele está associado a uma turma."}` (500) se houver turmas associadas.

#### Turmas (`/turmas`)

*   **`POST /turmas`**: Cria uma nova turma.
    *   **Corpo da Requisição (JSON)**:
        ```json
        {
            "nome": "Turma A - 2024",
            "professor_id": 1,
            "ativo": true
        }
        ```
    *   **Resposta**: `{"mensagem": "Turma criada com sucesso!"}` (201)
    *   **Erro**: `{"erro": "Professor não encontrado. Verifique o professor_id."}` (500) se o `professor_id` não existir.
*   **`GET /turmas`**: Lista todas as turmas.
    *   **Resposta**: `{"turmas": [...], "total_turmas": N}` (200)
*   **`GET /turmas/<int:id_turma>`**: Retorna os detalhes de uma turma específica.
    *   **Resposta**: `{"mensagem": "Turma encontrada com sucesso!", "dados_turma": {...}}` (200) ou `{"mensagem": "Turma não encontrada."}` (404)
*   **`PUT /turmas/<int:id_turma>`**: Atualiza os dados de uma turma.
    *   **Corpo da Requisição (JSON)**:
        ```json
        {
            "nome": "Turma B - 2024",
            "ativo": false
        }
        ```
    *   **Resposta**: `{"mensagem": "Turma atualizada com sucesso!"}` (200) ou `{"mensagem": "Turma não encontrada."}` (404)
*   **`DELETE /turmas/<int:id_turma>`**: Exclui uma turma.
    *   **Resposta**: `{"mensagem": "Turma deletada com sucesso!"}` (200) ou `{"mensagem": "Turma não encontrada."}` (404)

#### Alunos (`/alunos`)

*   **`POST /alunos`**: Cria um novo aluno.
    *   **Corpo da Requisição (JSON)**:
        ```json
        {
            "nome": "João Silva",
            "data_nascimento": "2008-05-15",
            "turma_id": 1,
            "nota_primeiro_semestre": 8.5,
            "nota_segundo_semestre": 7.0
        }
        ```
    *   **Observações**:
        *   `idade` é calculada automaticamente.
        *   `media_final` é calculada automaticamente se ambas as notas forem fornecidas.
        *   `data_nascimento` aceita formatos como "YYYY-MM-DD", "YYYY/MM/DD", "DD-MM-YYYY", "DD/MM/YYYY".
    *   **Resposta**: `{"mensagem": "Aluno criado com sucesso!"}` (201)
    *   **Erro**: `{"erro": "Turma não encontrada. Verifique o turma_id."}` (500) se o `turma_id` não existir.
*   **`GET /alunos`**: Lista todos os alunos.
    *   **Resposta**: `{"alunos": [...], "total_alunos": N}` (200)
*   **`GET /alunos/<int:id_aluno>`**: Retorna os detalhes de um aluno específico.
    *   **Resposta**: `{"mensagem": "Aluno encontrado com sucesso!", "dados_aluno": {...}}` (200) ou `{"mensagem": "Aluno não encontrado."}` (404)
*   **`PUT /alunos/<int:id_aluno>`**: Atualiza os dados de um aluno.
    *   **Corpo da Requisição (JSON)**:
        ```json
        {
            "nome": "João Pedro Silva",
            "nota_primeiro_semestre": 9.0
        }
        ```
    *   **Resposta**: `{"mensagem": "Aluno atualizado com sucesso!"}` (200) ou `{"mensagem": "Aluno não encontrado."}` (404)
*   **`DELETE /alunos/<int:id_aluno>`**: Exclui um aluno.
    *   **Resposta**: `{"mensagem": "Aluno deletado com sucesso!"}` (200) ou `{"mensagem": "Aluno não encontrado."}` (404)


## Estrutura do Projeto

```
API Flask - Monolitica Completa/
├── app.py                      # Ponto de entrada da aplicação Flask
├── config.py                   # Configurações da aplicação e do banco de dados
├── requirements.txt            # Dependências do projeto
├── controllers/                # Lógica de negócio e rotas da API
│   ├── aluno_control.py        # Endpoints para Alunos
│   ├── professor_control.py    # Endpoints para Professores
│   └── turma_control.py        # Endpoints para Turmas
├── helpers/                    # Funções auxiliares
│   ├── age_calculator.py       # Calcula a idade a partir da data de nascimento
│   └── date_converter.py       # Converte strings para objetos de data
├── models/                     # Definições dos modelos do banco de dados (SQLAlchemy)
│   ├── __init__.py             # Inicializa o objeto SQLAlchemy
│   ├── aluno.py                # Modelo Aluno
│   ├── professor.py            # Modelo Professor
│   └── turma.py                # Modelo Turma
└── instance/                   # Pasta para arquivos de instância (ex: database.db)
    └── database.db             # Banco de dados SQLite
```