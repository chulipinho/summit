import os
import logger 

log = logger.get_logger()

def clear_tmp():
    log.info("Clearing temporary files")
    files = os.listdir("tmp")

    for f in files:
        os.remove("tmp/" + f)

def format_summary(text):
    remove_list = [
        "##",
        "**",
    ]

    replace_list = {
        "*": "-"
    }

    for c in remove_list:
        text = text.replace(c, "")

    for c in replace_list:
        text = text.replace(c, replace_list[c])

    return text