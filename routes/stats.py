import schemas
import models
from fastapi import APIRouter, Body
from sqlalchemy import text
from database import engine
from datetime import datetime
from sqlalchemy.orm import sessionmaker 
from analysis import get_analysis


stats_router = APIRouter(
    prefix="/stats",
    tags=["stats"]
)

@stats_router.get("/")
async def get_stats():
    with sessionmaker(bind=engine)() as session:
        result = session.query(models.Stats).all()
        return result

@stats_router.post("/add_stats")
async def add_stats(stats: schemas.Stats = Body(...)):
    timestamp = datetime.now()
    with sessionmaker(bind=engine)() as session:
        new_stats = models.Stats(x=stats.x, y=stats.y, z=stats.z, device_id=stats.device_id, timestamp=timestamp)
        session.add(new_stats)
        session.commit()
    return {"message": "Stats added"}

@stats_router.get("/get_stats")
async def get_stats_analytics(start_date: str = '2000-01-01T00:00:00.000000', end_date: str = '2100-01-01T00:00:00.000000', device_id: int = 1):
    with sessionmaker(bind=engine)() as session:
        result = session.query(models.Stats).filter(models.Stats.timestamp.between(start_date, end_date), models.Stats.device_id == device_id).all()
        result = get_analysis(result)
        return result
    