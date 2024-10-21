from pydantic import BaseModel, field_validator
from pydantic.v1.utils import GetterDict

from peewee import ModelSelect

from typing import Any


class UserRequestModel(BaseModel):
    username: str
    password: str

    @field_validator('username')
    def username_validator(cls, username) -> str:
        if len(username) < 3 or len(username) > 50:
            raise ValueError('La longitud debe ser entre 4 y 50 caracteres')

        return username


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):

        res = getattr(self._obj, key, default)
        if isinstance(res, ModelSelect):
            return list(res)

        return res


class ResponseModel(BaseModel):
    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class UserResponseModel(ResponseModel):
    id: int
    username: str


class ReviewRequestModel(BaseModel):
    user_id: int
    movie_id: int
    review: str
    score: int


class ReviewResponseModel(ResponseModel):
    id: int
    movie_id: int
    review: str
    score: int


class MovieRequestModel(BaseModel):
    title: str
    year: int
    director: str


class MovieResponseModel(ResponseModel):
    id: int
    title: str
    year: int
    director: str

