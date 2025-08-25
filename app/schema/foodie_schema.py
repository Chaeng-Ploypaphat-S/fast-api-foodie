from pydantic import BaseModel, EmailStr

class FoodieCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class FoodieRead(BaseModel):
    id: int
    email: EmailStr
    username: str

    class Config:
        orm_mode = True
