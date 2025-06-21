from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import os

app = FastAPI(title="Sample FastAPI App", version="1.0.0")

class HealthResponse(BaseModel):
    status: str
    timestamp: datetime
    hostname: str

class ItemResponse(BaseModel):
    id: int
    name: str
    description: str

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI running in k3d!"}

@app.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now(),
        hostname=os.getenv("HOSTNAME", "unknown")
    )

@app.get("/api/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int):
    return ItemResponse(
        id=item_id,
        name=f"Item {item_id}",
        description=f"This is a sample item with ID {item_id}"
    )

@app.post("/api/items", response_model=ItemResponse)
async def create_item(item: ItemResponse):
    return item