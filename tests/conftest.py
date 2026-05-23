import os
import tempfile
import pytest
from src.app import create_app
from src.database import init_db

@pytest.fixture
def app():
    """
    Fixture do Pytest que configura e inicializa o aplicativo Flask para testes.
    Cria um arquivo de banco de dados SQLite temporário e isolado para cada teste,
    garantindo que um teste não influencie o resultado de outro.
    """
    # Cria um descritor de arquivo temporário seguro
    db_fd, db_path = tempfile.mkstemp()
    
    # Inicializa a aplicação injetando as configurações de teste
    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
        'SECRET_KEY': 'teste-chave-secreta-ambiente',
    })
    
    # Inicializa as tabelas do banco rodando o script schema.sql
    init_db(app)
    
    # Fornece o objeto de teste ao ambiente
    yield app
    
    # Teardown: Fecha o descritor e remove o arquivo físico temporário do disco
    os.close(db_fd)
    try:
        os.unlink(db_path)
    except OSError:
        pass

@pytest.fixture
def client(app):
    """
    Retorna o cliente de teste do Flask para simular requisições HTTP (GET/POST).
    """
    return app.test_client()

@pytest.fixture
def runner(app):
    """
    Retorna um executor de linha de comando para rodar comandos CLI caso necessário.
    """
    return app.test_cli_runner()
