from pydantic import BaseModel, Field, EmailStr, PositiveInt
from typing import Optional, List, Dict,
from datetime import datetime, time

class UserBase(BaseModel):
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    age: PositiveInt = Field(...)
    weight: Optional[PositiveInt] = None
    height: Optional[PositiveInt] = None
    fitness_goals:  Optional[str] = None
    medical_conditions:  Optional[str] = None
    activity_level:  Optional[str] = None



class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    username: Optional[str] = Field(...)
    email: Optional[EmailStr] = Field(...)
    password: Optional[str] = Field(...)
    age: Optional[PositiveInt] = Field(...)
    weight: Optional[PositiveInt] = None
    height: Optional[PositiveInt] = None
    fitness_goals:  Optional[str] = None
    medical_conditions:  Optional[str] = None
    activity_level:  Optional[str] = None


class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ExerciseBase(BaseModel):
    plan_name: str = Field(...)
    difficulty_level: Optional[str] = None
    duration : Optional[time]= None
    target_muscle_groups: Optional[str] = None 
    exercises_list : Optional[str] = None

class ExcerciseCreate(ExerciseBase):
    pass

class ExerciseUpdate(BaseModel):
    plan_name: Optional[str] = Field(...)
    difficulty_level: Optional[str] = None
    duration : Optional[time]= None
    target_muscle_groups: Optional[str] = None 
    exercises_list : Optional[str] = None


class ExerciseResponse(ExerciseBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

