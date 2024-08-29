from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional
from shared_structure.schemas.user import UserResponse 
from shared_structure.schemas.product import ProductResponse

class OrderBase(BaseModel):
    date: datetime
    quantity: int
    type: str

class OrderCreate(OrderBase):
    id_user: int
    id_product: int

class OrderUpdate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: int
    user: Optional[UserResponse] = None
    product: Optional[ProductResponse] = None

    model_config = ConfigDict(from_attributes=True)
