from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    name: str
    description: Optional[str]
    geom: str  # WKT (Well-Known Text)
    type: str # type of geometry, e.g., 'Point', 'Polygon'

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True