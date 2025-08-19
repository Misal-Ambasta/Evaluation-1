from fastapi import FastAPI
from database import create_tables
from contextlib import asynccontextmanager
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()

    yield



app = FastAPI(
    title="Fitness app",
    lifespan=lifespan
)

# app.include_router()

@app.get("/")
async def get_health():
    return {"message": "Fitness App"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
