from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class AdBase(BaseModel):
    status: bool = True
    amount: float
    link: str
    title: str
    image_url: Optional[str] = None
    start_date: datetime
    end_date: Optional[datetime] = None

class AdCreate(AdBase):
    id_user: int

class AdResponse(AdBase):
    id: int
    id_user: int

    model_config = ConfigDict(from_attributes=True)