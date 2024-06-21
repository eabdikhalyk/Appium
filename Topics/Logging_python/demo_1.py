import logging
logging.basicConfig(filename="test.log", level=logging.DEBUG)
logging.critical("This is critical")
logging.error("This is error")
logging.warning("This is warning")
logging.info("This is info")
logging.debug("This is a Debug")