import json
from unittest.mock import patch

from app.tests.conftest import (
    client,
    base_url,
    mock_response_get_popular_movies,
)

from app.infrastructure.client_impl.movie_client import MovieFavoritesClient


def test_get_popular_movies_OK(client, base_url):
    headers = {"Authorization": "Bearer 1234567890", "Content-Type": "application/json"}
    url = base_url + "/movies/popular"

    with patch(
        "app.domain.commands.handlers.handler_get_popular_movies"
    ) as mock_handler:
        mock_handler.return_value = mock_response_get_popular_movies
        response = client.get(url, headers=headers)

    assert response.status_code == 200
    assert response.json is not None
    assert len(response.json) == 20
    assert isinstance(response.json[0], dict)

def test_get_popular_movies_missing_token(client, base_url):
    headers = {"Content-Type": "application/json"}
    url = base_url + "/movies/popular"

    with patch(
        "app.domain.commands.handlers.handler_get_popular_movies"
    ) as mock_handler:
        response = client.get(url, headers=headers)
        mock_handler.assert_not_called()

    assert response.status_code == 401
    assert response.json is not None
    assert response.json["error"] == "Missing token"

def test_get_popular_movies_invalid_token(client, base_url):
    headers = {"Authorization": "Bearer Fake", "Content-Type": "application/json"}
    url = base_url + "/movies/popular"

    with patch(
        "app.domain.commands.handlers.handler_get_popular_movies"
    ) as mock_handler:
        response = client.get(url, headers=headers)
        mock_handler.assert_not_called()

    assert response.status_code == 401
    assert response.json is not None
    assert response.json["error"] == "Invalid token"

def test_add_favorite_movie_OK(client, base_url):
    headers = {"Authorization": "Bearer 1234567890"}
    url = base_url + "/movies/favorites"

    response = client.post(
        url,
        data=json.dumps({"movie_id": 933260}),
        content_type="application/json",
        headers=headers
    )

    assert response.status_code == 200
    assert response.json is not None
    assert response.json["id"] == 1
    assert isinstance(response.json["movie"], dict)
    assert response.json["movie"]["id"] == 933260
    assert response.json["movie"]["title"] == "The Substance"
    assert response.json["movie"]["overview"] == "A fading celebrity decides to use a black market drug, a cell-replicating substance that temporarily creates a younger, better version of herself."
    assert response.json["movie"]["vote_average"] == 7.362
    assert response.json["movie"]["vote_count"] == 513

def test_add_favorite_movie_missing_token(client, base_url):
    headers = {"Content-Type": "application/json"}
    url = base_url + "/movies/favorites"

    with patch(
        "app.domain.commands.handlers.handler_add_favorite_movie"
    ) as mock_handler:
        response = client.post(
            url,
            data=json.dumps({"movie_id": 933260}),
            content_type="application/json",
            headers=headers
        )
        mock_handler.assert_not_called()

    assert response.status_code == 401
    assert response.json is not None
    assert response.json["error"] == "Missing token"

def test_add_favorite_movie_invalid_token(client, base_url):
    headers = {"Authorization" : "Bearer Fake", "Content-Type": "application/json"}
    url = base_url + "/movies/favorites"

    with patch(
        "app.domain.commands.handlers.handler_add_favorite_movie"
    ) as mock_handler:
        response = client.post(
            url,
            data=json.dumps({"movie_id": 933260}),
            content_type="application/json",
            headers=headers
        )
        mock_handler.assert_not_called()

    assert response.status_code == 401
    assert response.json is not None
    assert response.json["error"] == "Invalid token"

def test_remove_favorite_movie_OK(client, base_url):
    headers = {"Authorization" : "Bearer 1234567890"}
    url = base_url + "/movies/favorites"

    #create the fake favorite
    favorite = MovieFavoritesClient().add_movie_favorite(2, 933260)

    assert favorite

    response = client.delete(
        url,
        data=json.dumps({"movie_id": 933260}),
        content_type="application/json",
        headers=headers
    )

    assert response.status_code == 200
    assert response.json is not None
    assert response.json["message"] == "Favorite removed"

def test_remove_favorite_movie_missing_token(client, base_url):
    headers = {"Content-Type": "application/json"}
    url = base_url + "/movies/favorites"

    with patch(
        "app.domain.commands.handlers.handler_remove_favorite_movie"
    ) as mock_handler:
        response = client.delete(
            url,
            data=json.dumps({"movie_id": 933260}),
            content_type="application/json",
            headers=headers
        )
        mock_handler.assert_not_called()

    assert response.status_code == 401
    assert response.json is not None
    assert response.json["error"] == "Missing token"

def test_remove_favorite_movie_invalid_token(client, base_url):
    headers = {"Authorization": "Bearer Fake", "Content-Type": "application/json"}
    url = base_url + "/movies/favorites"

    with patch(
        "app.domain.commands.handlers.handler_remove_favorite_movie"
    ) as mock_handler:
        response = client.delete(
            url,
            data=json.dumps({"movie_id": 933260}),
            content_type="application/json",
            headers=headers
        )
        mock_handler.assert_not_called()

    assert response.status_code == 401
    assert response.json is not None
    assert response.json["error"] == "Invalid token"

def test_get_favorite_movies_OK(client, base_url):
    headers = {"Authorization": "Bearer 1234567890", "Content-Type": "application/json"}
    url = base_url + "/movies/favorites"

    #Create the favorites
    MovieFavoritesClient().add_movie_favorite(2, 933260)
    MovieFavoritesClient().add_movie_favorite(2, 550988)

    response = client.get(url, headers=headers)

    assert response.status_code == 200
    assert response.json is not None
    assert len(response.json) == 2
    assert isinstance(response.json[0], dict)
