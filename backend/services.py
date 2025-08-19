from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import User, Exercise
from schemas import UserCreate, UserUpdate, UserResponse, ExcerciseCreate, ExerciseUpdate

# Create new user
async def user_create(db: AsyncSession, user: UserCreate) -> User:
    db_user = User(**user.model_dump())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

# Get a user details
async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    db_user = result.scalar_one_or_none()
    return db_user

# Update a user details
async def update_user(db: AsyncSession, user_id: int, user_update: UserUpdate):
    result = await db.execute(select(User).where(User.id == user_id))
    db_user = result.scalar_one_or_none()
    if db_user:
        update_data = user_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_user, field, value)
        await db.commit()
        await db.refresh(db_user)
    return db_user

# Delete a user
async def delete_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    db_user = result.scalar_one_or_none()
    if db_user:
        await db.delete(db_user)
        await db.commit()
        return True
    return False


# Create new exercise
async def exercise_create(db: AsyncSession, exercise: ExcerciseCreate) -> Exercise:
    db_exercise = Exercise(**exercise.model_dump())
    db.add(db_exercise)
    await db.commit()
    await db.refresh(db_exercise)
    return db_exercise

# Get a user details
async def get_exercise(db: AsyncSession, exercise_id: int):
    result = await db.execute(select(Exercise).where(Exercise.id == exercise_id))
    db_exercise = result.scalar_one_or_none()
    return db_exercise

async def get_all_exercise(db: AsyncSession, skip: int, limit: int = 100):
    result = await db.execute(select(Exercise).offset(skip).limit(limit))
    db_exercises = result.scalars().all()
    return db_exercises
# Update a exercise details
async def update_exercise(db: AsyncSession, exercise_id: int, exercise_update: ExerciseUpdate):
    result = await db.execute(select(Exercise).where(Exercise.id == exercise_id))
    db_exercise = result.scalar_one_or_none()
    if db_exercise:
        update_data = exercise_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_exercise, field, value)
        await db.commit()
        await db.refresh(db_exercise)
    return db_exercise

# Delete a exercise
async def delete_exercise(db: AsyncSession, exercise_id: int):
    result = await db.execute(select(Exercise).where(Exercise.id == exercise_id))
    db_exercise = result.scalar_one_or_none()
    if db_exercise:
        await db.delete(db_exercise)
        await db.commit()
        return True
    return False