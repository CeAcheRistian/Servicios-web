from pydantic import BaseModel, field_validator

class UserBaseModel(BaseModel):
    username: str
    password: str

    @field_validator('username')
    def username_validator(cls, username) -> str:
        if len(username) < 3 or len(username) > 50:
            raise ValueError('La longitud debe ser entre 4 y 50 caracteres')

        return username