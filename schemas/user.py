from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime
from app.schemas.device import DeviceResponse
from app.schemas.transfer import TransferResponse

class UserBase(BaseModel):
    email: str
    pseudo: str
    balance: float = 0.0
    token: Optional[str] = None
    refresh_token: Optional[str] = None
    daily_reward_claimed: bool = False
    expiration_date: Optional[datetime] = None

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    devices: List[DeviceResponse] = []
    Transfers: List[TransferResponse] = []

    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    email: str
    password: str

class TokenData(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str