from fastapi import APIRouter, HTTPException
from app.services.foodie_service import create_foodie
from app.services.auth_service import get_foodie_by_username
from app.foodie_schema import FoodieCreate, FoodieRead

router = APIRouter()

@router.post("/signup", response_model=FoodieRead)
def signup(foodie: FoodieCreate):
    result = create_foodie(foodie)
    if isinstance(result, dict) and "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result


@router.post("/login")
def login(foodie: FoodieCreate):
    if user := get_foodie_by_username(foodie.username):
        return {"message": "Login successful", "foodie": user}
    else:
        raise HTTPException(status_code=401, detail="Invalid username")