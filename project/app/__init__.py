from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter, Depends, HTTPException, status

from fastapi.security import OAuth2PasswordRequestForm

from .routers import user_router, review_router, movie_router

from .database import database as db
from .database import *

from .common import create_access_token

@asynccontextmanager
async def lifespan(app: FastAPI):
    if db.is_closed():
        db.connect()

    db.create_tables([User, Movie, UserReview])

    yield

    if not db.is_closed():
        db.close()
    print('Desconectando ...')

app = FastAPI(title='Reseñas de peliculas',
            description='Proyecto backend para reseñar peliculas.', version='1.0', lifespan=lifespan)

api_v1 = APIRouter(prefix='/api/v1')

api_v1.include_router(user_router)
api_v1.include_router(review_router)
api_v1.include_router(movie_router)

@api_v1.post('/auth')
async def auth(data: OAuth2PasswordRequestForm = Depends()):

    user = User.authenticate(data.username, data.password)

    if user:
        return {
            'access_token': create_access_token(user),
            'token_type': 'Bearer'
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Username o Password incorrectos',
            headers={'WWW-Authenticate': 'Beraer'}
        )
app.include_router(api_v1)

@app.get('/')
async def index():
    return "Hola mundo"











