from app.infrastructure.client_impl.tmdb_client import TMDBClient
from app.infrastructure.client_impl.movie_client import MovieFavoritesClient

def handler_get_popular_movies():
    client = TMDBClient()
    response = client.get_popular_movies()
    return response

def handler_add_favorite_movie(user_id: int, movie_id: int):
    client = MovieFavoritesClient()
    response = client.add_movie_favorite(user_id, movie_id)
    return response