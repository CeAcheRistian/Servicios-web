from typing import List

from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException

from database import database as db
from database import *

from schemas import UserRequestModel, UserResponseModel, ReviewRequestModel, ReviewResponseModel, MovieRequestModel, MovieResponseModel, ReviewRequestPutModel


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

    if User.select().where(User.id == user_review.user_id).first() is None:
        raise HTTPException(status_code=404, detail='Usuario no encontrado.')

    if Movie.select().where(Movie.id == user_review.movie_id).first() is None:
        raise HTTPException(status_code=404, detail='Pelicula no encontrada.')

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
        director=movie.director
    )
    return movie


@app.get('/reviews', response_model=List[ReviewResponseModel])
async def get_reviews():
    reviews = UserReview.select()

    return reviews


@app.get('/reviews/{review_id}', response_model=ReviewResponseModel)
async def get_review(review_id: int):
    user_review = UserReview.select().where(UserReview.id == review_id).first()

    if user_review is None:
        raise HTTPException(status_code=404, detail='Review no encontrada.')
    return user_review


@app.put('/reviews/{review_id}', response_model=ReviewResponseModel)
async def update_review(review_id: int, review_request: ReviewRequestPutModel):

    user_review = UserReview.select().where(UserReview.id == review_id).first()

    if user_review is None:
        raise HTTPException(status_code=404, detail='Review no encontrada.')

    user_review.review = review_request.review
    user_review.score = review_request.score
    user_review.save()

    return user_review


@app.delete('/reviews/{review_id}', response_model=ReviewResponseModel)
async def delete_review(review_id: int):
    user_review = UserReview.select().where(UserReview.id == review_id).first()

    if user_review is None:
        raise HTTPException(status_code=404, detail='Review no encontrada.')
    
    user_review.delete_instance()

    return user_review