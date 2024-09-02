movies = [
    # Malayalam Movies
    {
        "title": "Drishyam",
        "year": 2013,
        "language": "Malayalam",
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.6
    },
    {
        "title": "Premam",
        "year": 2015,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Bangalore Days",
        "year": 2014,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    # Tamil Movies
    {
        "title": "Kaala",
        "year": 2018,
        "language": "Tamil",
        "genres": ["Action", "Drama"],
        "rating": 7.3
    },
    {
        "title": "Vikram Vedha",
        "year": 2017,
        "language": "Tamil",
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 8.4
    },
    {
        "title": "Super Deluxe",
        "year": 2019,
        "language": "Tamil",
        "genres": ["Drama", "Mystery", "Thriller"],
        "rating": 8.3
    },
    # Hindi Movies
    {
        "title": "Dangal",
        "year": 2016,
        "language": "Hindi",
        "genres": ["Action", "Biography", "Drama"],
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "year": 2009,
        "language": "Hindi",
        "genres": ["Comedy", "Drama"],
        "rating": 8.4
    },
    {
        "title": "Gully Boy",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Drama", "Music"],
        "rating": 8.0
    }
]

# total_number_of_movies

movies_count=len(movies)
# print("Movie count",movies_count)

# movies with genre drama

genere_filter=[ m.get("title")  for m in movies if "Drama" in m.get("genres")]
# print(genere_filter)


# latest movie

def get_year(mov):

    return mov.get("year")

latest_movie_data=max(movies,key=get_year)

latest_movies=[m.get("title") for m in movies if m.get("year")==latest_movie_data.get("year")]
# print(latest_movies)
# top movies (movie with higest rating)

def get_rating(mov):

    return mov.get("rating")

top_movie_data=max(movies,key=get_rating)

top_rating_movies = [m.get("title") for m in movies if m.get("rating")==top_movie_data.get("rating")]

# print(top_rating_movies)

# movies with language malayalam

malayalam_movies=[m.get("title") for m in movies if m.get("language") =="Malayalam"]
# print(malayalam_movies)
# movies released after year 2016

year_filter=[m.get("title") for m in movies if m.get("year")>2016]
print(year_filter)

# movie with lowest rating
# malaylam movies with genere action
# movies release in same year
# oldest movie
# movie name with generes either drama or comedy