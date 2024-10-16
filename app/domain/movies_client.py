from abc import ABC, abstractmethod
from typing import List


class MoviesClient(ABC):
    @abstractmethod
    def get_popular_movies(self) -> List:
        raise NotImplementedError


class MovieFavoritesAbstractClient(ABC):
    @abstractmethod
    def add_movie_favorite(self, user_id: int, movie_id: int) -> dict:
        raise NotImplementedError

    @abstractmethod
    def remove_movie_favorite(self, user_id: int, movie_id: int) -> dict:
        raise NotImplementedError
