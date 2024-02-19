from fastapi import FastAPI
from database import Base, engine
from models import Stats
from routes import stats_router


app = FastAPI()

@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)

@app.get('/')
async def root():
    return {"message": "Gazprom-Neft backend trainee"}

app.include_router(stats_router)