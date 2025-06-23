from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry
from app.core.database import Base

from sqlalchemy.dialects.postgresql import JSON

class ItemV2(Base):
    __tablename__ = "itemsv2"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    geom = Column(Geometry("GEOMETRY", srid=4326))
    type = Column(String, nullable=True)
