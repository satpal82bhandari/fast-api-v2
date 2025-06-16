from app.dto.item import ItemCreate, ItemResponse
from app.persistence.item import add_item, get_item, get_items

async def add_item(itemCreate: ItemCreate) -> ItemResponse:
    db_item = await add_item(itemCreate)
    return ItemResponse.from_orm(db_item)


async def get_items():
    db_items = await get_items()
    return [ItemResponse.from_orm(db_item) for db_item in db_items]