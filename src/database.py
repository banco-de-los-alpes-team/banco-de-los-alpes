from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import os
from utils.logs import printLog
from dotenv import load_dotenv
load_dotenv()

database_user = os.getenv('POSTGRESQL_USER')
database_host = os.getenv('POSTGRESQL_HOST')
database_port = os.getenv('POSTGRESQL_PORT')
database_password = os.getenv('POSTGRESQL_PASSWORD')
database_name = os.getenv('DATABASE_NAME')

SQLALCHEMY_DATABASE_URL = ''

if database_host != None and database_name != None and database_password != None and database_user != None and database_port != None:
    SQLALCHEMY_DATABASE_URL = f'postgresql://{database_user}:{database_password}@{database_host}:{database_port}/{database_name}'
else:
    printLog('Database credentials not configured on envs')

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
metadata = Base.metadata # type: ignore

def get_db():
    db = SessionLocal()
    try: 
        yield db
    except:
        db.close()

