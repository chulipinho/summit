import os
import logger 

log = logger.get_logger()

def clear_tmp():
    log.info("Clearing temporary files")
    files = os.listdir("tmp")

    for f in files:
        os.remove("tmp/" + f)
