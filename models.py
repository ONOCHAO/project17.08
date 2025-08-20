from sqlalchemy import Column, Integer, String
from database import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    check = Column(Integer)
    status = Column(String, default="Новый")


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    descrip = Column(String)
    data = Column(String, unique=True)
    id_client = Column(Integer) 

class Personal(Base):
    __tablename__ = "Pers"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    password = Column(String, index=True)
