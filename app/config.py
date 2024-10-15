import os


class Config:
    DEBUG = True
    TMDB_API_KEY = ""
    TMDB_BASE_URL = "https://api.themoviedb.org/3/"
    REDIS_URL = "redis://127.0.0.1:6379/0"
    CACHE_TYPE = "redis"
    CACHE_DEFAULT_TIMEOUT = 30