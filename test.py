import logging
def log_test():
    logging.basicConfig(filename="test.log",level=logging.INFO,format="%(asctime)s %(filename)s %(funcName)s %(levelname)s %(message)s")
    logging.info("Hi, this is my info log!")

def log_test_object():

    # Creating the logger object and setting its level
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Define log format
    f_format = logging.Formatter("%(asctime)s %(filename)s %(funcName)s %(levelname)s %(message)s")

    # Define warning handler
    f_handler_warning = logging.FileHandler('test.warning.log')
    f_handler_warning.setFormatter(f_format)
    f_handler_warning.setLevel(logging.WARNING)

    # Define info handler
    f_handler_info = logging.FileHandler('test.info.log')
    f_handler_info.setFormatter(f_format)
    f_handler_info.setLevel(logging.INFO)

    # Adding handlers to the logger object
    logger.addHandler(f_handler_warning)
    logger.addHandler(f_handler_info)

    # Logging
    logger.info("Logging info using object!")
    logger.warning("Logging warning using object")
    logger.debug("Logging debug using object")

if __name__ == '__main__':
    log_test_object()