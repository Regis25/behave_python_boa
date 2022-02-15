import datetime
import logging
import os
from pathlib import Path


def setup():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s \t [%(levelname)s] | %(filename)s:%(lineno)s] > %(message)s")

    now = datetime.datetime.now()
    current_dir = str(Path().absolute())

    dir_name = "{}/log".format(current_dir)
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    file_handler = logging.FileHandler(dir_name + "/DEMO_" + now.strftime("%Y-%m-%d") + ".log")

    stream_handler = logging.StreamHandler()

    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
