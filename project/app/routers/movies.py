from fastapi import APIRouter

from ..database import Movie

from ..schemas import MovieRequestModel, MovieResponseModel

router =  APIRouter(prefix='/movies')

@router.post('', response_model=MovieResponseModel)
async def create_movies(movie: MovieRequestModel):

    movie = Movie.create(
        title=movie.title,
        year=movie.year,
        director=movie.director
    )
    return movie