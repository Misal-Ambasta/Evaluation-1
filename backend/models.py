# Store age, weight, height, fitness goals, medical conditions, activity level

from sqlalchemy import Column, Integer, String, Float, DateTime, Time, ForeignKey, Boolean
from database import Base
from sqlalchemy import func

class User(Base):
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True, index=True)
    username= Column(String(100), nullable=False, index=True)
    email=Column(String(100), nullable=False, index=True)
    password = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)
    height = Column(Float, nullable=False)
    fitness_goals = Column(String(100), nullable=False)
    medical_conditions = Column(String(200))
    activity_level = Column(String(50))
    create_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

# plan_name, difficulty_level, duration, target_muscle_groups, exercises_list
class Workout(Base):
    __tablename__ = "workout"

    Workout_id = Column(Integer, primary_key=True, index=True)
    plan_name = Column(String(100), nullable=False)
    difficulty_level = Column(String(100))
    duration = Column(Time)
    target_muscle_groups = Column(String(100))
    exercises_list = Column(String(100))

    user_table_id = Column(ForeignKey("user_table.id"))
    

# exercise_name, category, equipment_needed, difficulty, instructions, target_muscles

class Exercise(Base):
    __tablename__ = "exercise"

    exercise_id = Column(Integer, primary_key=True, index=True)
    exercise_name = Column(String(50), nullable=False)
    category = Column(String(50))
    equipment_needed = Column(Boolean, nullable=False, index=True)
    difficulty = Column(String(50), nullable=False, index=True)
    instructions = Column(String(200))
    target_muscles = Column(String(100))
    
    user_table_id = Column(ForeignKey("user_table.id"))

# user_id, workout_id, date, exercises_completed, sets, reps, weights, duration, calories_burned
class ProgressTracking(Base):
    __tablename__ = "progress_tracking"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime(timezone=True))
    exercises_completed = Column(Boolean)
    sets = Column(Integer)
    reps = Column(Integer)
    weights = Column(Integer)
    duration = Column(Time)
    calories_burned = Column(Integer)

    user_table_id = Column(ForeignKey("user_table.id"))
    Workout_id = Column(ForeignKey("workout.Workout_id"))


# user_id, date, meals, calories, macronutrients (protein, carbs, fats)
class nutrition(Base):
    __tablename__ = "nutrition"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    meals = Column(String(100))
    calories = Column(Integer)
    macronutrients = Column(Integer)

    user_table_id = Column(ForeignKey("user_table.id"))