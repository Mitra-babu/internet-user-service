from db.db_connection import base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String


class InternetUserTable(base):
    __tablename__ = 'internet_user'
    internet_user_id = Column(String, primary_key=True)
    country = Column(String)
    region = Column(String)
    population = Column(String)
    internet_user = Column(String)
    percentage_user = Column(String)
