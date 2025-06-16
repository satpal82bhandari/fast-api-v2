import os
from dotenv import load_dotenv
from app.services.item_service import add_item, get_all_items_service 

# Controller to list all items
async def list_items():
    # Await the coroutine from the service layer
    return await get_all_items_service()