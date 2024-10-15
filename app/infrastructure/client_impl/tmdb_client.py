import requests

from flask import current_app
from app.domain.movies_client import MoviesClient


class TMDBClient(MoviesClient):
    def __init__(self):
        self.api_key = current_app.config["TMDB_API_KEY"]
        self.base_url = current_app.config["TMDB_BASE_URL"]

    def construct_header(self):
        return {"accept": "application/json", "Authorization": f"Bearer {self.api_key}"}

    def get_popular_movies(self):
        url = f"{self.base_url}movie/popular"
        response = requests.get(url, headers=self.construct_header())
        response.raise_for_status()
        return response.json()["results"]
