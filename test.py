import requests
from collections import defaultdict


url = "https://api.themoviedb.org/3/genre/movie/list?api_key=c52d26892911f6d1bfc7c065be76b9d3&language=en-US"
get_genre = requests.get(url)
genre_dict = get_genre.json()['genres']

collect = defaultdict(dict)

for key in genre_dict:
    collect[key['id']] = key['name']


remade_genre_dict = dict(collect)


url_single_movie = "https://api.themoviedb.org/3/movie/76600?api_key=c52d26892911f6d1bfc7c065be76b9d3&language=en-US"

get_movie = requests.get(url_single_movie)
movie_dict = get_movie.json()['genres']
print(movie_dict)
testuoju = ""
for i in movie_dict:
    print(i['name'])
    testuoju += i['name'] + ", "
print(testuoju[:-2])