from moviepy.editor import *


def video(movie_id):

    clips = []

    audio_clip_1 = AudioFileClip(f"{movie_id}/{movie_id}_part_1.mp3")

    if os.path.exists(f"{movie_id}/{movie_id}_part_2.mp3"):
        audio_clip_2 = AudioFileClip(f"{movie_id}/{movie_id}_part_2.mp3")
        audio = concatenate_audioclips([audio_clip_1, audio_clip_2])
    else:
        audio = audio_clip_1

    clip_one = ImageClip(f'{movie_id}/{movie_id}.jpg').set_duration(audio.duration)
    clips.append(clip_one)

    video_clip = concatenate_videoclips(clips, method='compose')
    video_clip.audio = audio
    video_clip.write_videofile(f"{movie_id}/{movie_id}.mp4", fps=24,
                               remove_temp=True, codec="libx264", audio_codec="aac")
