from sqlalchemy import Column, String, Integer

from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    balance=Column(Integer)

class Card(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True, index=True)
    sender_name = Column(String, nullable=False)
    receiver_name = Column(String, nullable=False)
    balance = Column(Integer, nullable=False)
