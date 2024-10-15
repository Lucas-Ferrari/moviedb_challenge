from flask import Blueprint
from app.domain.commands.handlers import handler_get_popular_movies
from app.mock_auth import check_token

movies_bp = Blueprint("movies", __name__, url_prefix="/movies")


@movies_bp.route("/popular", methods=["GET"])
def get_popular_movies():
    user = check_token()
    if isinstance(user, tuple):
        return user

    res_movies = handler_get_popular_movies()
    return res_movies