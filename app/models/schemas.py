from pydantic import BaseModel


class Comic(BaseModel):
    comic_id: int


class User(BaseModel):
    user_id: int


class Rating(BaseModel):
    value: float | int