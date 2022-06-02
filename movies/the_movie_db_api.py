import environ

env = environ.Env()
environ.Env.read_env()

api_key = env("THE_MOVIE_DB_API_KEY")


class Endpoint:
    BASE = "https://api.themoviedb.org/3"
    GET_GENRES = f"{BASE}/genre/movie/list?api_key={api_key}&language=en-US"
    GET_MOVIES = f"{BASE}/discover/movie?api_key={api_key}&language=en-US&\
        sort_by=popularity.desc&include_adult=false&include_video=false&page=1&\
            with_watch_monetization_types=flatrate"
