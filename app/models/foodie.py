
from sqlalchemy import Column, Integer, String
from app.database.db import Base

class Foodie(Base):
    __tablename__ = "foodie"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    