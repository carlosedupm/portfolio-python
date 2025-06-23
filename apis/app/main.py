from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.routers import items_routers
from app.routers import auth_routers

app = FastAPI(title="Portfolio Python API",
              description="A simple API for managing a portfolio of items",
              version="1.0.0")

app.include_router(auth_routers.auth_router)
app.include_router(items_routers.item_router)
