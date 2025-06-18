# from app.persistence.db import BaseModelfrom pydantic import BaseModel
from pydantic import BaseModel
from uuid import UUID


class ItemCreate(BaseModel):
    name: str
    description: str | None = None  # Optional field

class ItemResponse(BaseModel):
    id: UUID
    name: str
    description: str

    class Config:
        from_attributes = True  # Required for Pydantic V2