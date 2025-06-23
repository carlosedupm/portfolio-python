
from fastapi import APIRouter

from pydantic import BaseModel
from app.schemas import Item


item_router = APIRouter(prefix="/items", tags=["items"])


@item_router.get("/", response_model=list[Item])
def list_items():
    return [{"id": 1, "name": "Notebook"}]
