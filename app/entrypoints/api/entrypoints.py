from flask import Blueprint, jsonify

from app.movies_app import cache

from app.domain.commands.handlers import handler_get_popular_movies
from app.mock_auth import check_token


movies_bp = Blueprint("movies", __name__, url_prefix="/movies")

@movies_bp.route("/popular", methods=["GET"])
def get_popular_movies():
    user = check_token()
    if isinstance(user, tuple):
        return user

    cached_movies = cache.get("popular_movies")
    if cached_movies:
        return jsonify(cached_movies), 200

    try:
        popular_movies_res = handler_get_popular_movies()
        cache.set("popular_movies", popular_movies_res, timeout=300000)
        return jsonify(popular_movies_res), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
