from app.infrastructure.client_impl.tmdb_client import TMDBClient
from app.infrastructure.client_impl.movie_client import MovieFavoritesClient, MovieRatingsClient

def handler_get_popular_movies():
    client = TMDBClient()
    response = client.get_popular_movies()
    return response

def handler_add_favorite_movie(user_id: int, movie_id: int):
    client = MovieFavoritesClient()
    response = client.add_movie_favorite(user_id, movie_id)
    return response

def handler_remove_favorite_movie(user_id: int, movie_id: int):
    client = MovieFavoritesClient()
    response = client.remove_movie_favorite(user_id, movie_id)
    return response

def handler_get_favorite_movies(user_id: int):
    client = MovieFavoritesClient()
    response = client.get_favorite_movies(user_id)
    return response

def handler_get_movie_ratings(user_id: int):
    client = MovieRatingsClient()
    response = client.get_movie_ratings(user_id)
    return response

def handler_add_movie_rating(user_id: int, movie_id: int, rating: int):
    client = MovieRatingsClient()
    response = client.add_movie_rating(user_id, movie_id, rating)
    return response

def handler_update_movie_rating(user_id: int, movie_id: int, rating: int):
    client = MovieRatingsClient()
    response = client.update_movie_rating(user_id, movie_id, rating)
    return response