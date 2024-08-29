from pydantic import BaseModel, ConfigDict
from datetime import datetime

class WorkBase(BaseModel):
    date: datetime
    uptime_amount: float = 0.0
    bonner_level: float = 0.0

class WorkCreate(WorkBase):
    id_device: int

class WorkResponse(WorkBase):
    id: int
    id_device: int

    model_config = ConfigDict(from_attributes=True)