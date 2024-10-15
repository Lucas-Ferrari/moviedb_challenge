from flask import Blueprint
from app.domain.commands.handlers import handler_get_popular_movies

movies_bp = Blueprint("movies", __name__, url_prefix="/movies")


@movies_bp.route("/popular", methods=["GET"])
def get_popular_movies():
    res_movies = handler_get_popular_movies()
    return res_movies