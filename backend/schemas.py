from pydantic import BaseModel, Field, EmailStr, PositiveInt


class UserBase(BaseModel):
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    age: PositiveInt = Field(...)
    weight: int = None