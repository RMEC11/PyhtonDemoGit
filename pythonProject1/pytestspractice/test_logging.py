import logging

def test_loggingDemo():
     logger = logging.getLogger(__name__)
     filehandler = logging.FileHandler("logging.log")
     formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
     filehandler.setFormatter(formatter)

     logger.addHandler(filehandler)

     logger.setLevel(logging.DEBUG)
     logger.debug("Debug level message")
     logger.info("Info level message")
     logger.warning("Warning level message")
     logger.error("Error level message")
     logger.critical("Critical level message")
