from config.database import Base
from sqlalchemy import Column, Integer, String, Float


class Movie(Base): #esta es una entidad en mi BBDD
    __tablename__ = 'movies' #nombre de la tabla

    #campos
    id = Column(Integer, primary_key= True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)