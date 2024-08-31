from pydantic import BaseModel, HttpUrl, ConfigDict
from typing import Optional
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from shared_structure.schemas.user import UserResponse  
    from shared_structure.schemas.game import GameResponse  
    from shared_structure.schemas.studio import StudioResponse  

class AdBase(BaseModel):
    status: bool = True
    amount: float
    link: HttpUrl
    title: str
    image_url: Optional[HttpUrl] = None
    start_date: datetime
    end_date: Optional[datetime] = None

class AdCreate(AdBase):
    id_user: int
    id_game: Optional[int] = None
    id_studio: Optional[int] = None

class AdUpdate(AdBase):
    status: Optional[bool] = None
    amount: Optional[float] = None
    link: Optional[HttpUrl] = None
    title: Optional[str] = None
    image_url: Optional[HttpUrl] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    id_game: Optional[int] = None
    id_studio: Optional[int] = None

class AdResponse(AdBase):
    id: int
    user: "UserResponse"
    game: Optional["GameResponse"] = None
    studio: Optional["StudioResponse"] = None

    model_config = ConfigDict(from_attributes=True)
