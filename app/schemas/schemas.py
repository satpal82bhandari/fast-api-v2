from pydantic import BaseModel
from typing import Optional, Dict, Any

class ItemBase(BaseModel):
    name: str
    description: Optional[str]
    geom: str  # WKT (Well-Known Text)
    # type: str # type of geometry, e.g., 'Point', 'Polygon'

class ItemCreate(ItemBase):
    geom: str      # keep this for any legacy single-item WKT POST if you still need it

class ItemCreateGeoJSON(ItemBase):
    geometry: Dict[str, Any]   # now accepts a GeoJSON object

class Item(ItemBase):
    id: int
    geometry: Dict[str, Any]   # returns GeoJSON

    class Config:
        from_attributes = True
        orm_mode = True