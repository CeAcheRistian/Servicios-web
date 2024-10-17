from pydantic import BaseModel, field_validator, ValidationError
from typing import Optional, Dict


class User(BaseModel):
    username: str
    password: str
    repeat_password: str
    age: Optional[int] = None

    @field_validator('username')
    def username_validation_length(cls, username) -> str:
        if len(username) < 3:
            raise ValueError('La longitud mínima es de 4 caracteres')

        elif len(username) > 50:
            raise ValueError('La longitud máxima es de 50 caracteres.')

        return username

    @field_validator('password', 'repeat_password')
    def repeat_password_validation(cls, password, repeat_password):

        if password != repeat_password:
            raise ValueError('Las contraseñas no coinciden')

        return 'repeat_password'


try:
    user1 = User(username='ernestina', password="pass123", repeat_password='pss123', age=27)

except ValidationError as e:
    print(e.json())
