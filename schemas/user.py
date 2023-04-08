from pydantic impot BaseModel

#info de usurio
class User(BaseModel):
    email:str
    password:str
