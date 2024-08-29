from pydantic import BaseModel, ConfigDict
from datetime import datetime

class TransferBase(BaseModel):
    date: datetime

class TransferCreate(TransferBase):
    id_user: int

class TransferResponse(TransferBase):
    id: int
    id_user: int

    model_config = ConfigDict(from_attributes=True)