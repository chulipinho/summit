from video import extract_audio
from ai import analize_audio
from drive import Drive

import os
from dotenv import load_dotenv

# todo: add log, convert response to json, send email

load_dotenv()
CLEAR_TMP = os.getenv("CLEAR_TMP", True)
VIDEO_PATH = os.getenv("VIDEO_PATH", "meetings")

def clear_tmp():
    files = os.listdir("tmp")

    for f in files:
        os.remove("tmp/" + f)

def app():
    path = VIDEO_PATH

    drive = Drive()
    drive.authorize()

    files = drive.get_content(path=path, mime_type="video")
    
    for f in files:
        path = "tmp/" + f["title"]
        f.GetContentFile(path)
        
        audio_path = extract_audio(path)
        res = analize_audio(audio_path)
        
        print(res)

    if CLEAR_TMP: clear_tmp()
    

if __name__ == "__main__":
    app()