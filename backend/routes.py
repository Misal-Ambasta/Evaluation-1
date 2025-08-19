from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
import services
from schemas import UserResponse, ExerciseResponse, ExerciseUpdate, ExcerciseCreate
from database import get_db

router = APIRouter()

# Get user detauls
@router.get("/users/", tags=["users"],  response_model=UserResponse, status_code=201)
async def get_a_users(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await services.get_user(user_id=user_id, db=db)
    return result

# Create Exercise
@router.post("/excercise/", tags=["excercise"],  response_model=ExerciseResponse, status_code=201)
async def exercise_create(exercise: ExcerciseCreate, db: AsyncSession = Depends(get_db)):
    result = await services.exercise_create(exercise=exercise, db=db)
    return result

#Get All exercise
@router.get("/excercise/all", tags=["excercise"],  response_model=ExerciseResponse, status_code=200)
async def get_all_exercise(skip:int, limit:int = 100, db: AsyncSession = Depends(get_db)):
    result = await services.get_all_exercise(skip=skip, limit=limit, db=db)
    return result

#Get A exercise
@router.get("/excercise/", tags=["excercise"],  response_model=ExerciseResponse, status_code=200)
async def get_a_exercises(exercise_id: int, db: AsyncSession = Depends(get_db)):
    result = await services.get_exercise(exercise_id=exercise_id, db=db)
    return result

# Update exercide
@router.put("/users/", tags=["excercise"],  response_model=ExerciseResponse, status_code=200)
async def update_exercise(exercise_id: int, exercise_update: ExerciseUpdate, db: AsyncSession = Depends(get_db)):
    result = await services.update_exercise(exercise_id=exercise_id, db=db, exercise_update=exercise_update)
    return result



# Delete Exercise
@router.delete("/excercise/", tags=["excercise"],  response_model=bool, status_code=200)
async def get_a_excercise(exercise_id: int, db: AsyncSession = Depends(get_db)):
    result = await services.delete_exercise(exercise_id=exercise_id, db=db)
    return result


