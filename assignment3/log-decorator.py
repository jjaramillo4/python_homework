# Task 1

import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger.log(logging.INFO, f"function: {func.__name__}")
        if args:
            logger.log(logging.INFO, f"positional parameters: {list(args)}")
        else:
            logger.log(logging.INFO, "positional parameters: none")
        if kwargs:
            logger.log(logging.INFO, f"keyword parameters: {kwargs}")
        else:
            logger.log(logging.INFO, "keyword parameters: none")    
        result = func(*args, **kwargs)
        logger.log(logging.INFO, f"return: {result}")
        return result
    return wrapper

@logger_decorator
def print_Hello():
    print("Hello, World!")

@logger_decorator
def take_args(*args):
    return True

@logger_decorator
def take_kwargs(**kwargs):
    return logger_decorator

print_Hello()
take_args(1, 2, 3, 4, 5)
take_kwargs(a=1, b=2, c=3, d=4, e=5)