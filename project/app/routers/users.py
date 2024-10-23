from fastapi import HTTPException, APIRouter, Response
from fastapi.security import HTTPBasicCredentials

from ..database import User

from ..schemas import UserRequestModel, UserResponseModel

router = APIRouter(prefix='/users')

@router.post('', response_model=UserResponseModel)
async def create_user(user: UserRequestModel) -> User:

    if User.select().where(User.username == user.username).exists():
        raise HTTPException(409, 'El nombre de usuario se encuentra en uso.')

    hashed_password = User.create_password(user.password)

    user = User.create(
        username=user.username,
        password=hashed_password
    )
    return user


@router.post('/login', response_model=UserResponseModel)
async def login(credentials: HTTPBasicCredentials, response: Response):
    
    user = User.select().where(User.username == credentials.username).first()

    if user is None:
        raise HTTPException(404, 'El usuario no fue encontrado.')
    
    if user.password != User.create_password(credentials.password):
        raise HTTPException(404, 'La contraseña no coincide.')
    
    response.set_cookie(key='user_id', value=user.id)

    return user