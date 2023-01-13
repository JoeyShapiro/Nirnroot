from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://admin:toor@nirnroot-db:3306/nirnroot?charset=utf8mb4")
db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class TableQuests(Base):
    __tablename__ = "quests"
    
    id = Column(Integer, primary_key=True)
    type = Column(String)
    title = Column(String)
    description = Column(String)
    parent_id = Column(Integer, ForeignKey('quests.id'))
    share = Column(Integer)
    secret = Column(Integer)

    tasks = relationship('TableQuests')
