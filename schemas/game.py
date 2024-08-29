from pydantic import BaseModel, HttpUrl, ConfigDict
from typing import Optional
from shared_structure.schemas.studio import StudioResponse
from datetime import datetime

class GameBase(BaseModel):
    name: str
    description: str
    image_url: HttpUrl
    link: HttpUrl
    rating: float

class GameCreate(GameBase):
    pass

class GameUpdate(GameBase):
    pass

class GameResponse(GameBase):
    id: int
    studio: Optional[StudioResponse] = None

    model_config = ConfigDict(from_attributes=True)
