from fastapi import APIRouter
from fastapi import Depends, Path, Query  #path: parametro de ruta, Query:parametros de busqueda
from fastapi.responses import JSONResponse #Para comandos HTLM, Para comandos Json
from pydantic import BaseModel, Field #permite crear esquema de datos, Field:validaciones
from typing import Optional, List 
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()

@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer)])#devolver 
def get_movies() -> List[Movie]:
    db= Session()
    result= MovieService(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

#ID movie
@movie_router.get('/movies/{id}',tags=['movies'], response_model=Movie,status_code=404) # Creación de parametros
def get_movie(id: int=Path(ge=1, le=2000)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie])#nueva ruta
#filtrado por query
def get_movies_by_category(category:str= Query(min_length=5, max_length=15)) -> List[Movie]:
    db= Session()
    result = MovieService(db).get_movies_by_category(category)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


#Metodo post registro
@movie_router.post('/movies/', tags=['movies'], response_model=dict,status_code=201) #el metodo body() sirve para traer el cuerpo de la peticion y no los parametros del query
def create_movie(movie:Movie) -> dict:
    #creacion de session para conexion a la BBDD
    db = Session()
    MovieService(db).create_movie(movie)
#    new_movie = MovieModel(**movie.dict()) #creacion de diccionario, se extraen los atributos y se pasan como parametros con los **
#    db.add(new_movie) #cargar a la BBDD
#    db.commit() #hacer una actualizacion para que los datos se guarden
    #movies.append(movie)
    return JSONResponse(status_code=201, content={'message': 'Se ha registrado la película'})

@movie_router.put('/movies/{id}', tags=['movies'],response_model=dict,status_code=200) 
def update_movie(id:int, movie:Movie)-> dict:
    #comprobacion de existencia
    db= Session()
    result = MovieService(db).get_movie(id)
    #db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    MovieService(db).update_movie(id, movie)
    return JSONResponse(status_code=200,content={'message': 'Se ha modificado la película'})
        
@movie_router.delete('/movies/{id}', tags=['movies'],response_model=dict, status_code=200)
def delete_movie(id:int) -> dict:
    db= Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={'message': 'Se ha eliminado la película'})