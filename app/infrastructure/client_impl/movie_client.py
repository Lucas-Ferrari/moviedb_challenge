from app.infrastructure.extensions import db

from app.domain.movies_client import MovieFavoritesAbstractClient
from app.domain.entities import MovieFavorites

class MovieFavoritesClient(MovieFavoritesAbstractClient):

    def add_movie_favorite(self, user_id, movie_id):
        favorite = MovieFavorites(movie_id=movie_id, user_id=user_id)
        db.session.add(favorite)
        db.session.commit()
        return favorite.to_dict()

    def remove_movie_favorite(self, user_id, movie_id):
        pass
