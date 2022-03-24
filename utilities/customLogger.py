import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename='.//Logs//test.log',format='%(asctime)s : %(levelname)s : %(message)s', datefmt='%m-%d-%Y %H:%M:%S',force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger