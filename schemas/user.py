from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime
from shared_structure.schemas.device import DeviceResponse
from shared_structure.schemas.transfer import TransferResponse

class UserBase(BaseModel):
    email: str
    username: str  # Aligner avec le modèle SQLAlchemy
    balance: float = 0.0
    token: Optional[str] = None
    refresh_token: Optional[str] = None
    daily_reward_claimed: bool = False
    expiration_date: Optional[datetime] = None
    is_admin: bool = False
    is_banned: bool = False
    experience: int = 0
    roblox_id: Optional[str] = None
    roblox_username: Optional[str] = None
    roblox_token: Optional[str] = None
    epic_games_id: Optional[str] = None
    epic_games_username: Optional[str] = None
    epic_games_token: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    devices: List[DeviceResponse] = []
    transfers: List[TransferResponse] = []

    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    email: str
    password: str

class TokenData(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
