
import logging

logging.basicConfig(level=logging.INFO)


def decorator(func):
    def logger():
        logging.info(f"Start the process ")
        func()
        logging.info(f"End process")
    return logger

@decorator
def saludar():
    logging.info(f"Hello there")


saludar()
