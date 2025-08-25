from app.models.foodie import Foodie
from app.database.db import SessionLocal
from app.foodie_schema import FoodieRead

def get_foodie_by_username(username: str):
    db = SessionLocal()
    db_foodie = db.query(Foodie).filter(Foodie.username == username).first()
    db.close()
    if db_foodie:
        return FoodieRead(id=db_foodie.id, username=db_foodie.username)
    return None
