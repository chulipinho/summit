import os

def clear_tmp():
    files = os.listdir("tmp")

    for f in files:
        os.remove("tmp/" + f)
