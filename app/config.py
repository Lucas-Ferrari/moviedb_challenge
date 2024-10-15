import os


class Config:
    API_KEY = os.getenv("TMDB_API_KEY")
    TMDB_URL = "https://api.themoviedb.org/"
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    CACHE_EXPIRY = int(os.getenv("CACHE_EXPIRY", 30))  # Tiempo de caché en segundos
