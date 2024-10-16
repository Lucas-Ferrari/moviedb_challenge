from datetime import datetime

from app.infrastructure.extensions import db


class MovieFavorites(db.Model):
    __tablename__ = "movie_favorites"

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"<MovieFavorites {self.id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "movie_id": self.movie_id,
            "user_id": self.user_id,
            "created_at": self.created_at
        }
