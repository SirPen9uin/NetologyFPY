import datetime
from functools import wraps


def time_check(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        start = datetime.datetime.now()
        result = old_function(*args, **kwargs)
        end = datetime.datetime.now()
        work_time = end - start
        print(f"Время работы функции {old_function.__name__} {work_time}")

        return result

    new_function.__name__ = old_function.__name__
    return new_function
