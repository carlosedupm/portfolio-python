from pydantic import BaseModel


class UserSchema(BaseModel):

    name: str
    email: str
    password: str
    active: bool = True
    roles: str = "user"


class ItemSchema(BaseModel):
    id: int
    name: str
