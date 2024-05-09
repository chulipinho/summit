import logging
import sys
import os
from dotenv import load_dotenv

load_dotenv()
LOG_PATH = os.getenv("LOG_PATH", "log/summit.log")

# Configure logger
log = logging.getLogger("Summit")

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)
logging.basicConfig(filename=LOG_PATH, level=logging.INFO)

def get_logger():
    return log