from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.routes.items import router as items_router # add router
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine, Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    
app = FastAPI(lifespan=lifespan)

# List here the exact origins your frontend uses:
origins = [
    "http://localhost:5173",   # Vite/React dev server
    "http://127.0.0.1:5173",   # sometimes the same
    # add more if needed (production URL, etc.)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # <-- allow those origins
    allow_credentials=True,
    allow_methods=["*"],             # allow GET, POST, etc.
    allow_headers=["*"],             # allow any headers
)

app.include_router(items_router, prefix="/items", tags=["items"]) # include router

@app.get("/")
def read_root():
    return {"Hello": "World"}
