from app.models.foodie import Foodie
from app.schema.foodie_schema import FoodieCreate, FoodieRead
from app.database.db import SessionLocal
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_all_foodies():
    db = SessionLocal()
    db_foodies = db.query(Foodie).all()
    db.close()
    return [FoodieRead(id=foodie.id, username=foodie.username) for foodie in db_foodies]

def create_foodie(foodie_data: FoodieCreate):
    db = SessionLocal()
    if (existing := db.query(Foodie).filter(Foodie.username == foodie_data['username']).first()):
        db.close()
        return {"error": "Username already exists"}
    db_foodie = Foodie(username=foodie_data['username'])
    db.add(db_foodie)
    db.commit()
    db.refresh(db_foodie)
    db.close()
    return FoodieRead(id=db_foodie.id, username=db_foodie.username)

def get_foodie(id: int):
    db = SessionLocal()
    db_foodie = db.query(Foodie).filter(Foodie.id == id).first()
    db.close()
    if db_foodie:
        return FoodieRead(id=db_foodie.id, username=db_foodie.username)
    return None