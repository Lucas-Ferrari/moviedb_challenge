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
        favorite = MovieFavorites.query.filter_by(user_id=user_id, movie_id=movie_id).first()
        db.session.delete(favorite)
        db.session.commit()
        return {"message": "Favorite removed"}

    def get_favorite_movies(self, user_id):
        favorites = MovieFavorites.query.filter_by(user_id=user_id).all()
        return [favorite.to_dict() for favorite in favorites]