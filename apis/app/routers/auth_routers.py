from fastapi import APIRouter, HTTPException


auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post("/login")
async def login(username: str, password: str):
    """Simulate a login endpoint.
    In a real application, you would validate the credentials against a database."""
    if username == "admin" and password == "secret":
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
