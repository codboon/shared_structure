from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional
from shared_structure.schemas.device import DeviceResponse  

class WorkBase(BaseModel):
    date: datetime
    uptime_amount: float = 0.0

class WorkCreate(WorkBase):
    id_device: int

class WorkUpdate(WorkBase):
    date: Optional[datetime] = None
    uptime_amount: Optional[float] = None
    id_device: Optional[int] = None

class WorkResponse(WorkBase):
    id: int
    device: DeviceResponse

    model_config = ConfigDict(from_attributes=True)
