from pydantic import BaseModel, EmailStr
from pydantic.config import ConfigDict
from typing import Optional, List
from datetime import datetime


###########################################################
#                       USER                              #
###########################################################
# BASE
class UserBase(BaseModel):
    email: EmailStr
    is_admin: Optional[bool] = False


# CREATE
class UserCreate(UserBase):
    username: str
    password: str

# TOKEN
class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

# READ
class UserOut(UserBase):
    id: int
    email: str
    username: str
    balance: float
    is_admin: bool
    is_banned: bool
    experience: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)

# UPDATE (patch)
class UserUpdate(UserBase):
    username: Optional[str]   = None
    password: Optional[str]   = None
    balance: Optional[float]  = None
    is_admin: Optional[bool]  = None
    is_banned: Optional[bool] = None
    experience: Optional[int] = None

# LOGIN
class UserLogin(BaseModel):
    email: EmailStr
    password: str



###########################################################
#                        AD                               #
###########################################################
class AdBase(BaseModel):
    id_user: int
    id_game: int

class AdCreate(AdBase):
    amount: float
    link: str
    title: str
    image_url: Optional[str] = None

class AdUpdate(AdBase):
    pass

class AdOut(AdBase):
    id: int
    status: str
    amount: float
    link: str
    title: str
    image_url: Optional[str] = None
    start_date: datetime
    end_date: Optional[datetime] = None
    plays: int = 0
    views: int = 0
    visits: int = 0
    ratings: int = 0

    model_config = ConfigDict(from_attributes=True)


###########################################################
#                       GAME                              #
###########################################################
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


###########################################################
#                       STUDIO                            #
###########################################################
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


###########################################################
#                       REVIEW                            #
###########################################################
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


###########################################################
#                      DEVICE                             #
###########################################################
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
    user: UserOut

    model_config = ConfigDict(from_attributes=True)

###########################################################
#                       WORK                              #
###########################################################
class WorkBase(BaseModel):
    date: datetime
    uptime_amount: float

class WorkCreate(WorkBase):
    id_device: int

class WorkOut(WorkBase):
    id: int
    id_device: int

    model_config = ConfigDict(from_attributes=True)



###########################################################
#                       ORDER                             #
###########################################################
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


###########################################################
#                       PRODUCT                           #
###########################################################
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