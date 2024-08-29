from pydantic import BaseModel, HttpUrl, ConfigDict
from typing import List, Optional
from shared_structure.schemas.order import OrderResponse  # Assure-toi que ce schéma existe

class ProductBase(BaseModel):
    name: str
    description: str
    image_url: HttpUrl
    price: float
    stock: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    orders: List[OrderResponse] = []

    model_config = ConfigDict(from_attributes=True)
