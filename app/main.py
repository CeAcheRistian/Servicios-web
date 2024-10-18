from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException

from database import database as db
from database import *

from schemas import UserBaseModel


@asynccontextmanager
async def lifespan(app: FastAPI):
    if db.is_closed():
        db.connect()

    db.create_tables([User, Movie, UserReview])

    yield

    if not db.is_closed():
        db.close()
    print('Desconectando ...')

app = FastAPI(title='Mi primer consumo de API',
            description='Proyecto para reseñar peliculas.', version='1.0', lifespan=lifespan)


@app.get('/')
async def index():
    return "Hola tonotos desmañanados"


@app.post('/users')
async def create_user(user: UserBaseModel):

    if User.select().where(User.username == user.username).exists():
        return HTTPException(409, 'El nombre de usuario se encuentra en uso.')

    hash_password = User.create_password(user.password)

    user = User.create(
        username=user.username,
        password=hash_password
    )
    return {
        'usuario': user.username,
        'id': user.id
    }
