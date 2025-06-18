from sqlalchemy import Column, Integer, String, Float
from app.persistence.db import Base  # Import Base from base.py

class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    # price = Column(Float)