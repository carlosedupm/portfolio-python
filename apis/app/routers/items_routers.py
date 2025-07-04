
from fastapi import APIRouter

from pydantic import BaseModel
from app.schemas import ItemSchema


item_router = APIRouter(prefix="/items", tags=["items"])


@item_router.get("/", response_model=list[ItemSchema])
def list_items():
    return [{"id": 1, "name": "Notebook"}]
