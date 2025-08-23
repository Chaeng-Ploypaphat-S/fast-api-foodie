from fastapi import FastAPI
from app.routes.foodie_routes import router as foodie_router
from app.database.db import Base, engine
from app.models.foodie import Foodie

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(foodie_router)