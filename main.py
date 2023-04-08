from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse #Para comandos HTLM, Para comandos Json
from pydantic import BaseModel #permite crear esquema de datos, Field:validaciones
from jwt_manager import create_token
from config.database import  engine, Base
from middlewares.error_handler import ErroHandler
from routers.movie import movie_router
from routers.user import user_router

#creación de una instacia de FastAPI
app= FastAPI()
app.title= 'Mi app con fastAPI' #cambiar el nombre del titulo
app.version = "0.0.1" #Cambiar la versión

#Middlewares
app.add_middleware(ErroHandler)

#Modificacion y busqueda de peliculas
app.include_router(movie_router)

#user: creacion
app.include_router(user_router)

#llamar Base
Base.metadata.create_all(bind=engine)



movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	},
    {
		"id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]

#creacion de un endpoint
@app.get('/', tags=['home'])#ruta de inicio
def message():
    return HTMLResponse('<h1>Hello World</h1>') #'Hello world' #mensaje

