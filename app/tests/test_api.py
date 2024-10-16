import json

from app.tests.conftest import (
    client,
    base_url
)


def test_add_favorite_movie(client, base_url):
    headers = {"Authorization": "Bearer 1234567890"}
    url = base_url + "/movies/favorites"

    response = client.post(
        url,
        data=json.dumps({"movie_id": 1}),
        content_type="application/json",
        headers=headers
    )

    assert response.status_code == 200
    assert response.json == {"message": "Movie added to favorites"}
