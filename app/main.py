from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException

from database import database as db
from database import *

from schemas import UserRequestModel, UserResponseModel, ReviewRequestModel, ReviewResponseModel, MovieRequestModel, MovieResponseModel


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


@app.post('/users', response_model=UserResponseModel)
async def create_user(user: UserRequestModel):

    if User.select().where(User.username == user.username).exists():
        return HTTPException(409, 'El nombre de usuario se encuentra en uso.')

    hashed_password = User.create_password(user.password)

    user = User.create(
        username=user.username,
        password=hashed_password
    )
    return user


@app.post('/reviews', response_model=ReviewResponseModel)
async def create_reviews(user_review: ReviewRequestModel):

    user_review = UserReview.create(
        user=user_review.user_id,
        movie=user_review.movie_id,
        review=user_review.review,
        score=user_review.score
    )
    return user_review


@app.post('/movies', response_model=MovieResponseModel)
async def create_movies(movie: MovieRequestModel):

    movie = Movie.create(
        title=movie.title,
        year=movie.year,
        director = movie.director
    )
    return movie