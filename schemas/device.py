from pydantic import BaseModel, ConfigDict
from typing import Optional, List

from app.schemas.work import WorkResponse

class DeviceBase(BaseModel):
    ip: str
    bonner_token: Optional[str] = None
    name: str
    uptime: float = 0.0
    status: bool = True

class DeviceCreate(DeviceBase):
    id_user: int

class DeviceResponse(DeviceBase):
    id: int
    id_user: int
    works: List[WorkResponse] = []
    model_config = ConfigDict(from_attributes=True)

class UptimeRequest(BaseModel):
    device_id: int
    uptime: float

class UptimeResponse(BaseModel):
    device_id: int
    total_uptime: float

class DeviceInfoRequest(DeviceBase):
    id_user: int

class RevenueCalculationRequest(BaseModel):
    device_id: int
    usage_time: float
    rate_per_second: float

class RevenueResponse(BaseModel):
    device_id: int
    calculated_revenue: float