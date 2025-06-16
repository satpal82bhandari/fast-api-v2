from app.persistence.db import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str | None = None  # Optional field

class ItemResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True  # Required for Pydantic V2