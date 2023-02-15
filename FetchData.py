import requests
from datetime import date
from datetime import datetime
import os

today = date.today()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

API_KEY = "c52d26892911f6d1bfc7c065be76b9d3"
IMAGE_URL = "https://image.tmdb.org/t/p/original"
API_URL = "https://api.themoviedb.org/3/movie"
EXAMPLE_URL_WITH_KEY = "https://api.themoviedb.org/3/movie/popular?api_key=c52d26892911f6d1bfc7c065be76b9d3&language=en-US&page=1"
IMDB_URL = "https://www.imdb.com/title/"

get_latest = "/latest"
get_now_playing = "/now_playing"
get_popular = "/popular"
get_to_rated = "/top_rated"
get_upcoming = "/upcoming"


def get_movie_by_id(movie_id: int):

    full_url = f"{API_URL}/{movie_id}?api_key={API_KEY}&language=en-US"
    get_movie = requests.get(full_url)

    if get_movie.status_code == 200:
        movie_dict = get_movie.json()

    mode = 0o666
    movie_dir = f"{movie_id}"
    path = os.path.join(movie_dir)
    if os.path.exists(path):
        print("Dir already exists")
    else:
        os.mkdir(path, mode)
        print("Directory '% s' created" % movie_dir)

    movie_poster_url = f"{IMAGE_URL}{movie_dict['poster_path']}"
    img_data = requests.get(movie_poster_url).content
    with open(f'{movie_dir}/{movie_id}.jpg', 'wb') as handler:
        handler.write(img_data)

    movie_file = open(f"{movie_id}/{movie_id}.txt", "a")
    clean_overview = movie_dict["overview"].replace('"','')
    content = f"{movie_dict['title']}, {clean_overview} rating is {str(movie_dict['vote_average'])[:3]}"

    if len(content) > 300:
        divided_content = []
        first_part = content[:300]
        second_part = content[300:]

        last_space_index = first_part.rfind(' ')

        if last_space_index != -1:
            first_part = content[:last_space_index]
            second_part = content[last_space_index:]
        divided_content.append(first_part)
        divided_content.append(second_part)
        for line in divided_content:
            movie_file.write(line + '\n')
    else:
        movie_file.write(content)
        movie_file.close()

    genres = ""
    for i in movie_dict['genres']:
        genres += i['name'] + ", "

    tik_tok_caption_file = open(f"{movie_id}/tiktokcaption.txt", "a")
    tik_tok_caption_content = f"Short movie overview of {movie_dict['title']}," \
                              f" rating {str(movie_dict['vote_average'])[:3]}, genres: {genres[:-2]}"
    tik_tok_caption_file.write(tik_tok_caption_content)
    print(tik_tok_caption_content)
    tik_tok_caption_file.close()
