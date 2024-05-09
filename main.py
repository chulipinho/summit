import logger
from video import extract_audio
from ai import analize_audio
from drive import Drive
from utils import clear_tmp
from dotenv import load_dotenv

import os

# todo: 
# - convert response to json 
# - send email

# Load environment variables
load_dotenv()
CLEAR_TMP = my_env = os.getenv("CLEAR_TMP", 'true').lower() in ('true', '1', 't')
VIDEO_PATH = os.getenv("VIDEO_PATH", "meetings")
LOG_PATH = os.getenv("LOG_PATH", "log/summit.log")

def app():  
    path = VIDEO_PATH

    log = logger.get_logger()
    log.info("adler")

    # Log into user's google drive
    drive = Drive()
    drive.authorize()

    files = drive.get_content(path=path, mime_type="video")
    
    # Download files from drive, extract audio and sends to AI Studio.
    for f in files:
        path = "tmp/" + f["title"]
        f.GetContentFile(path)
        
        audio_path = extract_audio(path)
        res = analize_audio(audio_path)
        
        print(res)

    if CLEAR_TMP: clear_tmp()
    

if __name__ == "__main__":
    app()