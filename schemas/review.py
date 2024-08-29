from pydantic import BaseModel, ConfigDict
from typing import Optional
from shared_structure.schemas.user import UserResponse
from shared_structure.schemas.game import GameResponse

class ReviewBase(BaseModel):
    rating: float
    content: str

class ReviewCreate(ReviewBase):
    id_user: int
    id_game: int

class ReviewUpdate(ReviewBase):
    pass

class ReviewResponse(ReviewBase):
    id: int
    user: Optional[UserResponse] = None
    game: Optional[GameResponse] = None

    model_config = ConfigDict(from_attributes=True)
