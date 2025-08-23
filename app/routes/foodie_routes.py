
from fastapi import APIRouter
from app.services.foodie_service import get_foodie, create_foodie, get_all_foodies

router = APIRouter()


@router.get("/foodie/{id}")
def read_foodie(id: int):
    return get_foodie(id)

@router.get("/foodies")
def read_all_foodies():
    return get_all_foodies()

@router.post("/foodie")
def add_foodie(foodie_data: dict):
    return create_foodie(foodie_data)