from sqlalchemy import Column, Float, DateTime, Integer
from database import Base


class Stats(Base):
    __tablename__ = "stats"

    id = Column(Integer, primary_key=True, index=True)
    x = Column(Float)
    y = Column(Float)
    z = Column(Float)
    device_id = Column(Integer)
    timestamp = Column(DateTime)