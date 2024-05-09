from video import extract_audio
from ai import analize_audio
from drive import Drive

import os
from dotenv import load_dotenv

# todo: add log, remove files from temp folder, convert response to json, send email

# runs only if file is main

def app():
    load_dotenv()
    path = os.getenv("VIDEO_PATH")

    drive = Drive()
    drive.authorize()

    
    files = drive.get_content(path=path, mime_type="video")
    
    for f in files:
        path = "tmp/" + f["title"]
        f.GetContentFile(path)
        
        audio_path = extract_audio(path)
        res = analize_audio(audio_path)
        
        print(res)
    

if __name__ == "__main__":
    app()