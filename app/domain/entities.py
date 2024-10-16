from datetime import datetime

from app.infrastructure.extensions import db


class MovieFavorites(db.Model):
    __tablename__ = "movie_favorites"

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    movie = db.relationship("Movies", backref="favorites", lazy=True)

    def __repr__(self):
        return f"<MovieFavorites {self.id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "movie": self.movie.to_dict(),
            "user_id": self.user_id,
            "created_at": self.created_at
        }


class Movies(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    overview = db.Column(db.Text, nullable=False)
    popularity = db.Column(db.Float, nullable=False)
    release_date = db.Column(db.Text, nullable=False)
    vote_average = db.Column(db.Float, nullable=False)
    vote_count = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"<Movie {self.id} - {self.title}>"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "overview": self.overview,
            "popularity": self.popularity,
            "release_date": self.release_date,
            "vote_average": self.vote_average,
            "vote_count": self.vote_count
        }

    @classmethod
    def get_or_create(cls, **kwargs):
        instance = cls.query.filter_by(id=kwargs["id"]).first()
        if instance:
            return instance
        else:
            instance = Movies(
                id=kwargs["id"],
                title=kwargs["title"],
                overview=kwargs["overview"],
                popularity=kwargs["popularity"],
                release_date=kwargs["release_date"],
                vote_average=kwargs["vote_average"],
                vote_count=kwargs["vote_count"],
            )
            db.session.add(instance)
            db.session.commit()
            return instance


class MovieRating(db.Model):
    __tablename__ = "movie_ratings"

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    movie = db.relationship("Movies", backref="ratings", lazy=True)

    def __repr__(self):
        return f"<MovieRating {self.id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "movie": self.movie.to_dict(),
            "user_id": self.user_id,
            "rating": self.rating,
            "created_at": self.created_at
        }