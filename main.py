import logger
from video import extract_audio
from ai import analize_audio
from drive import Drive
from utils import clear_tmp
from dotenv import load_dotenv
from mail import Mail

import os

# todo: 
# - Format mail

# Load environment variables
load_dotenv()
CLEAR_TMP = my_env = os.getenv("CLEAR_TMP", 'true').lower() in ('true', '1', 't')
VIDEO_PATH = os.getenv("VIDEO_PATH", "meetings")
LOG_PATH = os.getenv("LOG_PATH", "log/summit.log")

def app():  
    path = VIDEO_PATH

    log = logger.get_logger()

    user_input = input("Insira os e-mails(separados por espaço) que irão receber os resumos das reuniões: ")
    emails = user_input.split(" ")

    # Log into user's google drive
    drive = Drive()
    drive.authorize()

    files = drive.get_content(path=path, mime_type="video")
    
    summaries = []

    # Download files from drive, extract audio and sends to AI Studio.
    for f in files:
        path = "tmp/" + f["title"]
        f.GetContentFile(path)
        
        audio_path = extract_audio(path)
        res = analize_audio(audio_path)
        
        summary_title = ".".join(f["title"].split(".")[:-1])
        summaries.append(f"{summary_title}:\n{res}")

    email_content = "Aqui estão os resumos desta semana:\n\n\n"
    email_content += "\n".join(summaries)

    # Send e-mail with summaries
    mail = Mail()
    mail.send(email_content, "Resumos da semana", emails)

    if CLEAR_TMP: clear_tmp()

if __name__ == "__main__":
    app()