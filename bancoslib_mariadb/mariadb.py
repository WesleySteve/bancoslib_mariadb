import os

import dotenv
import sqlalchemy



def connect_db_mariadb(dotenv_path=os.path.expanduser("~/.env")):
    """Função para se conectar no banco de dados

    Args:
        dotenv_path (caminho das variaveis de ambiente, optional):
        pesquisa .env iniciando na raiz do usuario caso ele não passe um caminho.
        caminho padrão: os.path.expanduser("~/.env").

    Returns:
        conexao: retorna a conexao com o banco de dados mariadb
    """

    # carregando o dotenv
    dotenv.load_dotenv(dotenv_path)

    # importando as variaveis de ambiente
    _host = os.getenv("MARIADB_HOST")
    _port = os.getenv("MARIADB_PORT")
    _user = os.getenv("MARIADB_USER")
    _paswd = os.getenv("MARIADB_ROOT_PASSWORD")
    _db = os.getenv("MARIADB_DATABASE")
    
    
    # definindo string de conexao com o banco de dados postgres
    str_connection = f"mysql+pymysql://{_user}:{_paswd}@{_host}:{_port}/{_db}"

    # criando a conexao com o banco de dados postgres
    con = sqlalchemy.create_engine(str_connection)
    
    
    return con
