from pydantic import BaseModel


class AccessTokenRequest(BaseModel):
    access_token: str


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
