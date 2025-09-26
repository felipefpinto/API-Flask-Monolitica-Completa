import os
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlite3 import Connection as SQLite3Connection

class Config:               
    # tipo do banco e a sua localização (arquivo)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    #  desabilita o recurso de o SQLAlchemy monitorar e emitir sinais quando um objeto é alterado, o que é a prática recomendada
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # chave secreta e única usada pelo Flask para a segurança da aplicação, assinar os cookies de sessão e proteger formulários
    SECRET_KEY = os.urandom(24)
    
    # Forçar o SQLite a validar chaves estrangeiras
    @event.listens_for(Engine, "connect")
    def set_sqlite_pragma(dbapi_connection, connection_record):
        if isinstance(dbapi_connection, SQLite3Connection):
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON;")
            cursor.close()
