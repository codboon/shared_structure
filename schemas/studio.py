from pydantic import BaseModel, HttpUrl, ConfigDict
from typing import Optional, List
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from shared_structure.schemas.game import GameResponse
    from shared_structure.schemas.ad import AdResponse

class StudioBase(BaseModel):
    name: str
    description: str
    image_url: HttpUrl
    link: HttpUrl
    rating: float
    color: str

class StudioCreate(StudioBase):
    pass

class StudioUpdate(StudioBase):
    pass

class StudioResponse(StudioBase):
    id: int
    games: List["GameResponse"] = []
    ads: List["AdResponse"] = []

    model_config = ConfigDict(from_attributes=True)
