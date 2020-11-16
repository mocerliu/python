from sqlalchemy import Column, Integer, String
from studentMangerWeb.database import Base,db_session

from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


# example: User
# 自动生成
class User(Base):
    __tablename__ = 'users'
    query = db_session.query_property()
    eid = Column(INTEGER(11), primary_key=True)
    userName = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

    def __init__(self, name=None, pwd=None):
        self.userName = name
        self.password = pwd

    def __repr__(self):
        return '<User %r>' % (self.name)