import os #interactuar con el sistema operativo
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name  = '../database.sqlite' #nombre de la BBDD
base_dir  = os.path.dirname(os.path.realpath(__file__)) #Leer el directorio actual

#url de la BBDD
database_url= f'sqlite:///{os.path.join(base_dir, sqlite_file_name)}'

#motor de la BBDD
engine = create_engine(database_url, echo=True)

#creacion de sesion para conexion de base dedatos
Session= sessionmaker(bind=engine)

#manipulacion de todas las tablas de las BBDD
Base = declarative_base()