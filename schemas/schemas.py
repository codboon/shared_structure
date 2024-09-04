from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from pydantic.config import ConfigDict

# Shared schemas
class UserBase(BaseModel):
    email: EmailStr
    username: str
    balance: Optional[float] = 0.0
    is_admin: Optional[bool] = False
    is_banned: Optional[bool] = False
    experience: Optional[int] = 0

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

# Game schemas
class GameBase(BaseModel):
    name: str
    description: str
    image_url: str
    link: str
    rating: float

class GameCreate(GameBase):
    pass

class GameOut(GameBase):
    id: int
    studio_id: int
    visits: int = 0
    plays: int = 0
    ratings: int = 0

    model_config = ConfigDict(from_attributes=True)

# Studio schemas
class StudioBase(BaseModel):
    name: str
    description: str
    image_url: str
    link: str
    rating: float
    color: str

class StudioCreate(StudioBase):
    creator_id: int

class StudioOut(StudioBase):
    id: int
    games: List[GameOut] = []
    creator_id: int

    model_config = ConfigDict(from_attributes=True)

# Review schemas
class ReviewBase(BaseModel):
    rating: float
    content: str

class ReviewCreate(ReviewBase):
    id_user: int
    id_game: int
    id_ad: int

class ReviewOut(ReviewBase):
    id: int
    id_user: int
    id_game: int
    id_ad: int

    model_config = ConfigDict(from_attributes=True)

# Product schemas
class ProductBase(BaseModel):
    name: str
    description: str
    image_url: str
    price: float
    stock: int
    currency: str

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

# Order schemas
class OrderBase(BaseModel):
    date: datetime
    type: str

class OrderCreate(OrderBase):
    id_user: int
    id_product: int

class OrderOut(OrderBase):
    id: int
    id_user: int
    id_product: int

    model_config = ConfigDict(from_attributes=True)

# Ad schemas
class AdBase(BaseModel):
    amount: float
    link: str
    title: str
    status: Optional[bool] = True
    start_date: datetime
    end_date: Optional[datetime] = None

class AdCreate(BaseModel):
    id_user: int
    id_game: Optional[int] = None
    id_studio: int
    amount: float
    link: str
    title: str
    image_url: Optional[str]  # Assure-toi que ce champ est bien défini
    start_date: datetime
    end_date: Optional[datetime]

class AdOut(BaseModel):
    id: int
    id_user: int
    id_game: Optional[int]
    id_studio: int
    amount: float
    link: str
    title: str
    image_url: Optional[str]
    start_date: datetime
    end_date: Optional[datetime]

    # Ajout des champs avec des valeurs par défaut de 0
    plays: int = 0
    views: int = 0
    visits: int = 0
    ratings: int = 0

    model_config = ConfigDict(from_attributes=True)


# Device schemas
class DeviceBase(BaseModel):
    ip: str
    bonner_token: Optional[str] = None
    name: str
    uptime: float
    status: Optional[bool] = True

class DeviceCreate(DeviceBase):
    id_user: int

class DeviceOut(DeviceBase):
    id: int
    id_user: int

    model_config = ConfigDict(from_attributes=True)

# Work schemas
class WorkBase(BaseModel):
    date: datetime
    uptime_amount: float

class WorkCreate(WorkBase):
    id_device: int

class WorkOut(WorkBase):
    id: int
    id_device: int

    model_config = ConfigDict(from_attributes=True)
