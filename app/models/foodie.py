
from sqlalchemy import Column, Integer, String, Boolean
from app.database.db import Base

class Foodie(Base):
    __tablename__ = "foodie"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)  # Store hashed password in production
    is_active = Column(Boolean, default=True)