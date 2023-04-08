from models.movie import Movie as MovieModel
from schemas.movie import Movie

class MovieService():
    
    def __init__(self, db) -> None: #Se le enviara un sesion a la BBDD
        self.db = db

    def get_movies(self):
        restult = self.db.query(MovieModel).all()
        return result

    def get_movie(self,id):
        restult = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result
    
    def get_movies_by_category(self,category):
        restult = self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return result

    def create_movie(sefl,movie:Movie):
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return

    def update_movie(self,id: int, data: Movie):
        movie = self.db.query(MovieModel).filter(MovieModel.id== id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating
        movie.category = data.category
        self.db.commit()
        return