import logging
import sys

class logger:
    loggingEnabled = False
    initialised = False
    path = ""
    name = ""
    handler = None

    def __init__(self):
        if logger.initialised == False:
            logger.setup()

    @staticmethod
    def setup(to_console = True, to_file = False, name = "LOCAL"):
        logger.handler = logging.getLogger()
        logger.handler.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
        ## Setup Console Logging..
        if to_console == True:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.handler.addHandler(console_handler)

        if to_file != False:
            file_handler = logging.FileHandler(to_file)
            file_handler.setFormatter(formatter)
            logger.handler.addHandler(file_handler)

            # logger = logging.getLogger('timeloop')
            # ch = logging.StreamHandler(sys.stdout)
            # ch.setLevel(logging.INFO)
            # formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
            # ch.setFormatter(formatter)
            # logger.addHandler(ch)
            # logger.setLevel(logging.INFO)
            # #self.logger = logger

    @staticmethod
    def set_enabled(status):
        logger.loggingEnabled = status

    @staticmethod
    def debug(str):
        if logger.loggingEnabled:
            logger.handler.debug(str)

    @staticmethod
    def info(str):
        if logger.loggingEnabled:
            logger.handler.info(str)

    @staticmethod
    def error(str):
        if logger.loggingEnabled:
            logger.handler.error(str)


# logger.setup(to_console=False, to_file="./test.log")
# logger.info("blahblah")