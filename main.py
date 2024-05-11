import logger
from video import extract_audio
from ai import analize_audio
from utils import clear_tmp, format_summary
from google_services import GoogleServices

from dotenv import load_dotenv
import os

# todo: 
# - user interface

# Load environment variables
load_dotenv()
CLEAR_TMP = my_env = os.getenv("CLEAR_TMP", 'true').lower() in ('true', '1', 't')
VIDEO_PATH = os.getenv("VIDEO_PATH", "meetings")
LOG_PATH = os.getenv("LOG_PATH", "log/summit.log")

def app():
    path = VIDEO_PATH

    user_input = input("Insira os e-mails(separados por espaço) que irão receber os resumos das reuniões: ")
    emails = user_input.split(" ")

    google_service = GoogleServices()

    # Log into user's google drive
    drive = google_service.drive
    files = drive.get_content(path=path, mime_type="video")
    
    summaries = []

    # Download files from drive, extract audio and sends to AI Studio.
    for f in files:
        path = "tmp/" + f["name"]
        f_id = f["id"]

        drive.download_file(f_id, path)
        
        audio_path = extract_audio(path)
        res = analize_audio(audio_path)
        
        summary_title = ".".join(f["name"].split(".")[:-1])
        summaries.append(format_summary(f"{summary_title} {res}:"))

    email_content = "Aqui estão os resumos desta semana:\n\n"
    email_content += "\n\n\n".join(summaries)

    # Send e-mail with summaries
    mail = google_service.mail
    mail.send(email_content, "Resumos da semana", emails)

    if CLEAR_TMP: clear_tmp()

if __name__ == "__main__":
    app()