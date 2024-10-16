
# Movies app challenge

This project is a coding challenge using Flask, hexagonal architecture, sqlite3 and redis for cache.




## Run Locally

Clone the project

```bash
  git clone https://github.com/Lucas-Ferrari/moviedb_challenge
```

Go to the project directory

```bash
  cd moviedb_challenge
```

Create a virtualenv

```bash
  python3 -m venv .venv
```

Activate the environment

```bash
    source .venv/bin/activate
```

Install the dependencies

```bash
    pip install -r requirements.txt
```

Run the server (note the debug flag, only for development purposes):
```bash
    flask --app app/movies_app run --debug --port 8000
```
## Running Tests

Confirm you have the environment activated and run:

```bash
  pytest .
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`TMDB_API_KEY` = Register in themoviedb.org and get your key from your account settings
