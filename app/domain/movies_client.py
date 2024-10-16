from abc import ABC, abstractmethod
from typing import List


class MoviesClient(ABC):
    @abstractmethod
    def get_popular_movies(self) -> List:
        raise NotImplementedError

    @abstractmethod
    def get_movie_details(self, movie_id: int) -> dict:
        raise NotImplementedError


class MovieFavoritesAbstractClient(ABC):
    @abstractmethod
    def add_movie_favorite(self, user_id: int, movie_id: int) -> dict:
        raise NotImplementedError

    @abstractmethod
    def remove_movie_favorite(self, user_id: int, movie_id: int) -> dict:
        raise NotImplementedError

    @abstractmethod
    def get_favorite_movies(self, user_id: int) -> List:
        raise NotImplementedError


class MovieRatingsAbstractclient(ABC):
    @abstractmethod
    def get_movie_ratings(self, user_id: int) -> List:
        raise NotImplementedError

    @abstractmethod
    def add_movie_rating(self, user_id: int, movie_id: int, rating: int) -> dict:
        raise NotImplementedError

    @abstractmethod
    def update_movie_rating(self, user_id: int, movie_id: int, rating: int) -> dict:
        raise NotImplementedError
