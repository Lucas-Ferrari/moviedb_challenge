DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS movies_favourites;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  token TEXT NOT NULL
);

CREATE TABLE movies (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE movies_favourites (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  movie_id INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user (id),
  FOREIGN KEY (movie_id) REFERENCES movies (id)
);