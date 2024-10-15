from abc import ABC, abstractmethod
from typing import List


class MoviesClient(ABC):
    @abstractmethod
    def get_popular_movies(self) -> List:
        raise NotImplementedError