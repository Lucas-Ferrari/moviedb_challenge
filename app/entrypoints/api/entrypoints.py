from flask import Blueprint, jsonify, request

from app.movies_app import cache
from app.mock_auth import check_token

from app.domain.commands.handlers import (
    handler_get_popular_movies,
    handler_add_favorite_movie,
    handler_remove_favorite_movie,
    handler_get_favorite_movies,
)


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
        cache.set("popular_movies", popular_movies_res, timeout=30)
        return jsonify(popular_movies_res), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@movies_bp.route("/favorites", methods=["POST"])
def add_favorite_movie():
    user = check_token()
    if isinstance(user, tuple):
        return user

    movie_id = request.json.get("movie_id", None)

    if movie_id is None:
        return jsonify({"error": "movie_id is required"}), 400

    try:
        response = handler_add_favorite_movie(user["id"], movie_id)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@movies_bp.route("/favorites", methods=["DELETE"])
def remove_favorite_movie():
    user = check_token()
    if isinstance(user, tuple):
        return user

    movie_id = request.json.get("movie_id", None)

    if movie_id is None:
        return jsonify({"error": "movie_id is required"}), 400

    try:
        response = handler_remove_favorite_movie(user["id"], movie_id)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@movies_bp.route("/favorites", methods=["GET"])
def get_favorite_movies():
    user = check_token()
    if isinstance(user, tuple):
        return user

    try:
        response = handler_get_favorite_movies(user["id"])
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
