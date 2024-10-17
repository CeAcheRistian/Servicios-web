from contextlib import asynccontextmanager
from fastapi import FastAPI

from database import database as db
from database import *


@asynccontextmanager
async def lifespan(app: FastAPI):
    if db.is_closed():
        db.connect()
    
    db.create_tables([User,Movie,UserReview])

    yield

    if not db.is_closed():
        db.close()
    print('Desconectando ...')

app = FastAPI(title='Mi primer consumo de API',
            description='Proyecto para reseñar peliculas.', version='1.0', lifespan=lifespan)


@app.get('/')
async def index():
    return "Hola tonotos desmañanados"
