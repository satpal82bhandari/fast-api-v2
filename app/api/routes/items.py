from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.crud.crud import create_item_geojson, get_items_geojson
import csv
import json

router = APIRouter()

@router.post("/")
async def upload_csv(file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed.")

    content = await file.read()
    text = content.decode("utf-8")
    reader = csv.DictReader(text.splitlines())

    for row in reader:
        try:
            geojson = json.loads(row["geom"])  # must be a valid GeoJSON string
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail=f"Invalid geometry JSON: {row['geom']}")

        await create_item_geojson(
            db=db,
            name=row["name"],
            description=row["description"],
            geometry=geojson,
            type=row["type"],
        )

    return {"status": 201, "message": "CSV uploaded successfully."}


@router.get("/")
async def get_items(db: AsyncSession = Depends(get_db)):
    return await get_items_geojson(db)
