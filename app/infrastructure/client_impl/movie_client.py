from app.infrastructure.extensions import db

from app.domain.movies_client import MovieFavoritesAbstractClient, MovieRatingsAbstractclient
from app.domain.entities import MovieFavorites, Movies, MovieRating
from app.infrastructure.client_impl.tmdb_client import TMDBClient

class MovieFavoritesClient(MovieFavoritesAbstractClient):

    def add_movie_favorite(self, user_id, movie_id):
        tmdb_client = TMDBClient()
        movie = tmdb_client.get_movie_details(movie_id)

        favorite = MovieFavorites(
            movie_id=movie_id,
            user_id=user_id
        )

        movie = Movies.get_or_create(
            id=movie["id"],
            title=movie["title"],
            overview=movie["overview"],
            popularity=movie["popularity"],
            release_date=movie["release_date"],
            vote_average=movie["vote_average"],
            vote_count=movie["vote_count"],
        )

        db.session.add(favorite)
        db.session.commit()
        return favorite.to_dict()

    def remove_movie_favorite(self, user_id, movie_id):
        favorite = MovieFavorites.query.filter_by(user_id=user_id, movie_id=movie_id).first()
        if not favorite:
            return {"message": "Favorite not found"}
        db.session.delete(favorite)
        db.session.commit()
        return {"message": "Favorite removed"}

    def get_favorite_movies(self, user_id):
        favorites = MovieFavorites.query.filter_by(user_id=user_id).all()
        return [favorite.to_dict() for favorite in favorites]


class MovieRatingsClient(MovieRatingsAbstractclient):

    def get_movie_ratings(self, user_id: int):
        ratings = MovieRating.query.filter_by(user_id=user_id).all()
        return [rating.to_dict() for rating in ratings]


    def add_movie_rating(self, user_id: int, movie_id: int, rating: int):
        tmdb_client = TMDBClient()
        movie = tmdb_client.get_movie_details(movie_id)

        movie_rating = MovieRating(movie_id=movie_id, user_id=user_id, rating=rating)

        movie = Movies.get_or_create(
            id=movie["id"],
            title=movie["title"],
            overview=movie["overview"],
            popularity=movie["popularity"],
            release_date=movie["release_date"],
            vote_average=movie["vote_average"],
            vote_count=movie["vote_count"],
        )

        db.session.add(movie_rating)
        db.session.commit()
        return movie_rating.to_dict()

    def update_movie_rating(self, user_id: int, movie_id: int, rating: int):
        movie_rating = MovieRating.query.filter_by(user_id=user_id, movie_id=movie_id).first()

        if not movie_rating:
            return {"message": f"Could not update rating for movie {movie_id}, you have to add a rating first"}

        movie_rating.rating = rating
        db.session.commit()
        return movie_rating.to_dict()