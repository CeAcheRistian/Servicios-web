from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter

from .routers import user_router, review_router, movie_router

from .database import database as db
from .database import *


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

api_v1 = APIRouter(prefix='/api/v1')

api_v1.include_router(user_router)
api_v1.include_router(review_router)
api_v1.include_router(movie_router)

app.include_router(api_v1)

@app.get('/')
async def index():
    return "Hola tonotos desmañanados"











