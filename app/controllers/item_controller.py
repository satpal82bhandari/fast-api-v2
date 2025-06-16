import os
from dotenv import load_dotenv
from app.services.item_service import add_item, get_items 

# Controller to list all items
async def get_items():
    # Await the coroutine from the service layer
    return await get_items()