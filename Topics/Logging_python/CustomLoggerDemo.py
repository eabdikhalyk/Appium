from Topics import Logging_python as cl


class CustomLoggerDemo():
    log = cl.customLogger()

    def methodeOne(self):
        self.log.critical("This is  a critical 1")
        self.log.error("This is a error 1")
        self.log.warning("This is a warning 1")
        self.log.info("This is a info 1")
        self.log.debug("This is a debug 1")

    def methodTwo(self):
        m2 = cl.customLogger()
        m2.critical("This is  a critical 2")
        m2.error("This is a error 2")
        m2.warning("This is a warning 2")
        m2.info("This is a info 2")
        m2.debug("This is a debug 2")

cld = CustomLoggerDemo()
cld.methodeOne()
cld.methodTwo()