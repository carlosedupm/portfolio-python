from fastapi import APIRouter, HTTPException, Depends
from app.schemas import UserSchema
from sqlalchemy.orm import Session
from app.models import User
from app.dependencies import get_session

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post("/register")
async def register(user_schema: UserSchema, session=Depends(get_session)):
    """Register a new user."""
    new_user = User(
        name=user_schema.name,
        email=user_schema.email,
        password=user_schema.password,
        active=user_schema.active,
        roles=user_schema.roles
    )
    session.add(new_user)
    session.commit()
    return {"message": "User registered successfully"}


@auth_router.post("/login")
async def login(user_schema: UserSchema, session: Session = Depends(get_session)):
    """Log in an existing user."""
    user = session.query(User).filter(User.name == user_schema.name).first()
    if user and user.password == user_schema.password:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
