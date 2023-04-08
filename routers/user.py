from fastapi import APIRouter
from pydantic import BaseModel
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
from schemas.user import User
user_router = APIRouter()

@user_router.post('/login', tags=['auth']) #recibir datos y confirmacion de usuario
def login(user: User,status_code=200):
    if user.email == 'admin@gmail.com' and user.password=='admin':
        token:str=create_token(user.dict())
    return JSONResponse(status_code=200, content=token)