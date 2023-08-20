from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlalchemy_database_url = '{engine}://{user}:{password}@{host}:{port}/{database}'.format(
    engine='postgresql+psycopg2',
    user="postgres",
    password="nopassword",
    host="localhost",
    port="5432",
    database="internet"
)
engine = create_engine(sqlalchemy_database_url, echo=True)
session_local = sessionmaker(bind=engine, autocommit=False, autoflush=False)
base = declarative_base()


def get_connection():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

# if __name__=="__main__":
#     get_connection
