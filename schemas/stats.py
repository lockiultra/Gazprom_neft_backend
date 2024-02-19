from pydantic import BaseModel

class Stats(BaseModel):
    x: float
    y: float
    z: float
    device_id: int