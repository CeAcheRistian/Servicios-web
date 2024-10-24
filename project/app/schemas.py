from pydantic import BaseModel, field_validator
from pydantic.v1.utils import GetterDict

from peewee import ModelSelect

from typing import Any


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default_value: Any = None):

        res = getattr(self._obj, key, default_value)
        if isinstance(res, ModelSelect):
            return list(res)

        return res


class ResponseModel(BaseModel):
    class Config:
        from_attributes = True
        getter_dict = PeeweeGetterDict


"""------------User----------------"""


class UserRequestModel(BaseModel):
    username: str
    password: str

    @field_validator('username')
    def username_validator(cls, username) -> str:

        if len(username) < 3 or len(username) > 50:
            raise ValueError('La longitud debe ser entre 4 y 50 caracteres')

        return username


class UserResponseModel(ResponseModel):
    id: int
    username: str


"""------------Movies----------------"""


class MovieRequestModel(BaseModel):
    title: str
    year: int
    director: str


class MovieResponseModel(ResponseModel):
    id: int
    title: str
    year: int
    director: str


"""------------Reviews----------------"""


class ReviewFieldValidator():

    @field_validator('score')
    def score_validator(cls, score) -> int:

        if score < 1 or score > 10:
            raise ValueError('Solo se permiten valores entre el 1 y 10.')

        return score


class ReviewRequestModel(BaseModel, ReviewFieldValidator):
    # user_id: int Ahora es cachado por medio de un token
    movie_id: int
    review: str
    score: int


class ReviewResponseModel(ResponseModel):
    id: int
    user: UserResponseModel
    movie: MovieResponseModel
    review: str
    score: int


class ReviewRequestPutModel(BaseModel, ReviewFieldValidator):
    review: str
    score: int
