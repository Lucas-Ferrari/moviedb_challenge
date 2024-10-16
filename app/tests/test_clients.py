from unittest.mock import patch

from app.infrastructure.client_impl.movie_client import MovieFavoritesClient
from app.infrastructure.client_impl.tmdb_client import TMDBClient

from app.tests.conftest import (
    client,
)


def test_init_client(client):
    tmdb_client = TMDBClient()
    assert tmdb_client.api_key
    assert tmdb_client.base_url == "https://api.themoviedb.org/3/"
    assert isinstance(tmdb_client, TMDBClient)
    assert isinstance(tmdb_client.api_key, str)

def test_init_client_no_env(client):
    with patch("app.infrastructure.client_impl.tmdb_client.current_app") as mock_app:
        mock_app.config = {}
        tmdb_client = TMDBClient()
        assert tmdb_client.api_key is None
        assert tmdb_client.base_url is None

def test_get_popular_movies(client):
    tmdb_client = TMDBClient()
    response = tmdb_client.get_popular_movies()
    assert response is not None
    assert len(response) == 20
    assert isinstance(response[0], dict)
