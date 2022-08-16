import logging

DEBUG = logging.DEBUG
INFO = logging.INFO
ERROR = logging.ERROR

class LogToFile:
    def __init__(self, level = DEBUG, filename = "debug.log", mode = "w"):
        self.level = level
        self.filename = filename
        self.mode = mode

    def log(self, msg, level = DEBUG):
        FORMAT  = "%(asctime)-15s%(message)s"
        logging.basicConfig(filemode = self.mode, filename=self.filename, format = FORMAT, level = level)
        if level == DEBUG:
            logging.debug(msg)
        elif level == INFO:
            logging.info(msg)
        elif level == ERROR:
            logging.error(msg)