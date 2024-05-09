from video import extract_audio
from ai import analize_audio
from drive import Drive

import os

# todo: add log, remove files from temp folder, convert response to json, send email

# runs only if file is main
if __name__ == "__main__":
    drive = Drive()
    drive.authorize()

    path = os.getenv("VIDEO_PATH")
    files = drive.get_content(path=path, mime_type="video")
    
    for f in files:
        path = "tmp/" + f["title"]
        f.GetContentFile(path)
        
        audio_path = extract_audio(path)
        res = analize_audio(audio_path)
        
        print(res)