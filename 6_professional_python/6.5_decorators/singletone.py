from functools import wraps


def singletone(old_function):
    instance = None

    @wraps(old_function)
    def new_function(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = old_function(*args, **kwargs)
        return instance

    return new_function


@singletone
def get_conncetion():
    return "connection"


get_conncetion()
get_conncetion()
