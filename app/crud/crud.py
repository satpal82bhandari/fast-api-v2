from shapely.geometry import shape
from geoalchemy2.shape import from_shape
from app.models.models import ItemV2  # Use the new table
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from geoalchemy2.shape import to_shape

async def create_item_geojson(db: AsyncSession, name: str, description: str, geometry: dict, type: str):
    try:
        shapely_geom = shape(geometry)
    except Exception as e:
        raise Exception(f"Invalid GeoJSON shape: {e}")

    db_item = ItemV2(
        name=name,
        description=description,
        geom=from_shape(shapely_geom, srid=4326),
        type=type,
    )
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item

async def get_items_geojson(db: AsyncSession):
    result = await db.execute(select(ItemV2))
    items = result.scalars().all()

    result_data = []
    for item in items:
        shape_obj = to_shape(item.geom)
        result_data.append({
            "id": item.id,
            "name": item.name,
            "description": item.description,
            "type": item.type,
            "geom": shape_obj.__geo_interface__,  # returns GeoJSON dict
        })

    return result_data
