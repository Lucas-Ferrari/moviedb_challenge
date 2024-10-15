from flask import Blueprint


movies_bp = Blueprint("movies", __name__, url_prefix="/movies")


@movies_bp.route("/popular", methods=["GET"])
def get_popular_movies():
    return "popular movies"