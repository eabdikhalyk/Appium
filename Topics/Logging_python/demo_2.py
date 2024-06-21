import logging
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', filename="test2.log", datefmt='%d/%m/%y %I:%M:%S %p %A', level=logging.DEBUG)
logging.critical("This is critical")
logging.error("This is error")
logging.warning("This is warning")
logging.info("This is info")
logging.debug("This is a Debug")