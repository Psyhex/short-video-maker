import FetchData
import Tts
import Video
import time


def create_movie(movie_id: int):
    FetchData.get_movie_by_id(movie_id)
    time.sleep(3)
    Tts.get_tts(movie_id)
    time.sleep(3)
    Video.video(movie_id)
    print("Video created successfully")


create_movie(436270)
