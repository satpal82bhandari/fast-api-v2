from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.dto.item import ItemCreate, ItemResponse
from app.controllers.item_controller import add_item, get_items

router = APIRouter()

@router.post("/items/", response_model=ItemResponse)
async def create_item(item_data: ItemCreate):
    return await add_item(item_data)

'''
@router.get("/items/{item_id}", response_model=ItemResponse)
async def read_item(item_id: int):
    return await get_item_by_id(item_id)
'''

@router.get("/items/")
async def get_all_items_in_memory():
    return await get_items()