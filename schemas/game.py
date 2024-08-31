from pydantic import BaseModel, HttpUrl, ConfigDict
from typing import Optional
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from shared_structure.schemas.studio import StudioResponse

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
    studio: Optional["StudioResponse"] = None  # Utilisation de la chaîne de caractères pour retarder l'importation

    model_config = ConfigDict(from_attributes=True)
