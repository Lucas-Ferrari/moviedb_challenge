from app.infrastructure.client_impl.tmdb_client import TMDBClient


def handler_get_popular_movies():
    client = TMDBClient()
    response = client.get_popular_movies()
    return response