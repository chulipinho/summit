import logging
import sys
import os
from dotenv import load_dotenv

if not os.path.exists("log"):
    os.makedirs("log")

load_dotenv()
LOG_PATH = os.getenv("LOG_PATH", "log/summit.log")

# Configure logger
log = logging.getLogger("Summit")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)

logging.basicConfig(filename=LOG_PATH, level=logging.DEBUG)
log.addHandler(handler)

def get_logger():
    return log

if __name__ == "__main__":
    log = get_logger()
    log.info("This is a test")
    log.debug("adler")