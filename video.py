from moviepy.editor import VideoFileClip
import os

def get_audio_path(video_path):
    path_arr = video_path.split("/")
    title = path_arr[-1].split(".")[0]
    audio_path = "/".join(path_arr[:-1]) + f"/{title}.mp3"

    return audio_path    

def extract_audio(video_path):
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file {video_path} not found")

    audio_path = get_audio_path(video_path)
    if os.path.exists(audio_path):
        os.remove(audio_path)

    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)

    video.close()
    audio.close()

    return audio_path

if __name__ == "__main__":
    # path = "tmp/Product Marketing Meeting (weekly) 2021-06-28 (480p).mp4"
    # # os.remove(path)
    # audio_path = extract_audio(path)
    # print(f"Audio file saved to {audio_path}")
    pass