from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.persistence.db import SessionLocal  # Import Base from base.py
from app.models.item import Item  # No circular dependency now
from dotenv import load_dotenv
from app.dto.item import ItemCreate
import os

async def add_item_to_db(item_data: ItemCreate):
     with SessionLocal() as session:
        try:
            db_item = Item(**item_data.dict())  # Assuming item_data is a Pydantic model
            session.add(db_item)
            session.commit()
            session.refresh(db_item)
            return db_item
        finally:
            session.close()

async def get_item(item_id):
     with SessionLocal() as session:
        try:
            db_item = session.query(Item).filter(Item.id == item_id).first()
            return db_item
        finally:
            session.close()

async def get_items():
     with SessionLocal() as session:
        try:
            db_items = session.query(Item).all()
            return db_items
        finally:
            session.close()