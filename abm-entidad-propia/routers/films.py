from fastapi import APIRouter, HTTPException, status
from models.films import (
    Films,
    CreateFilmResponse,
    GetFilmsResponse,
    DeleteFilmResponse,
    UpdateFilmResponse
)
from typing import List

router = APIRouter()

peliculas = [
    Films(id= 1, name="El Padrino", rating=9, year=1972, studio="Paramount Pictures"),
    Films(id= 2, name="Interestelar", rating=8, year=2014, studio="Warner Bros."),
    Films(id= 3, name="El Viaje de Chihiro", rating=9, year=2001, studio="Studio Ghibli"),
    Films(id= 4, name="Parásitos", rating=8, year=2019, studio="CJ Entertainment"),
    Films(id= 5, name="Matrix", rating=8, year=1999, studio="Warner Bros.")
]

@router.get('/films/')
def get_films() -> GetFilmsResponse:
    return GetFilmsResponse(filmsList= peliculas)

@router.get('/films/{rating}')
def get_by_rating(rating: int) -> GetFilmsResponse:
    filmsList: List[Films] = []
    if rating < 0 or rating > 10:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='El rating debe ser positivo y menor o igual a 10.')

    for film in peliculas:
        if film.rating == rating:
            filmsList.append(film)

    return GetFilmsResponse(filmsList= filmsList)

@router.post('/films')
def create_film(film: Films) -> CreateFilmResponse:

    if film.rating < 0 or film.rating > 10:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='El rating debe ser positivo y menor o igual a 10.')
    if film.year < 1970 or film.year > 2026:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='El año de la película no es válido (1970 - 2026).')

    peliculas.append(film)
    return CreateFilmResponse(message= 'Película añadida con éxito.')

@router.delete('/films/{id}')
def delete_film(id: int) -> DeleteFilmResponse:
    filmToDelete: Films | None = None
    for film in peliculas:
        if film.id == id:
            filmToDelete = film

    if filmToDelete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Película no encontrada.')

    peliculas.remove(filmToDelete)
    return DeleteFilmResponse(message=f'Película con id {id} borrada.')

@router.put('/films/{id}')
def update_film(id: int,
                name: str | None = None,
                rating: int | None = None,
                year: int | None = None,
                studio: str | None = None) -> UpdateFilmResponse:

    message: str = f'Actualizaciones de la película con id {id} |'
    filmToUpdate: Films | None = None
    for film in peliculas:
        if film.id == id:
            filmToUpdate = film

    if filmToUpdate is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Película no encontrada.')


    if name:
        filmToUpdate.name = name
        message += f' Nombre actualizado a {name} |'
    if rating:
        if rating < 0 or rating > 10:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='El rating debe ser positivo y menor o igual a 10.')
        filmToUpdate.rating = rating
        message += f' Rating actualizado a {rating} |'
    if year:
        if year < 1970 or year > 2026:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='El año de la película no es válido (1970 - 2026).')
        filmToUpdate.year = year
        message += f' Año actualizado a {year} |'
    if studio:
        filmToUpdate.studio = studio
        message += f' Estudio actualizado a {studio} |'

    return UpdateFilmResponse(message= message)