from pydantic import BaseModel
from typing import List

class Films(BaseModel):
    id: int
    name: str
    rating: int
    year: int
    studio: str

class GetFilmsResponse(BaseModel):
    filmsList: List[Films]

class CreateFilmResponse(BaseModel):
    message: str

class DeleteFilmResponse(BaseModel):
    message: str

class UpdateFilmResponse(BaseModel):
    message: str