from pydantic import BaseModel

class FoodieCreate(BaseModel):
    username: str

class FoodieRead(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True