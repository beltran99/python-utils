import time
import datetime

def exec_time(func):
    """
    Decorator that prints the execution time of a function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        formatted_time = str(datetime.timedelta(seconds=execution_time))
        print(f'Execution time of {func.__name__}: {formatted_time}')
        return result
    return wrapper