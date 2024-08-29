from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from shared_structure.schemas.user import UserResponse
from shared_structure.schemas.work import WorkResponse

class DeviceBase(BaseModel):
    ip: str
    bonner_token: Optional[str] = None
    name: str
    uptime: float = 0.0
    status: bool = True

class DeviceCreate(DeviceBase):
    id_user: int

class DeviceUpdate(DeviceBase):
    ip: Optional[str] = None
    bonner_token: Optional[str] = None
    name: Optional[str] = None
    uptime: Optional[float] = None
    status: Optional[bool] = None

class DeviceResponse(DeviceBase):
    id: int
    user: UserResponse
    works: List[WorkResponse] = []

    model_config = ConfigDict(from_attributes=True)
