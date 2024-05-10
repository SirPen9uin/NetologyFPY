import time
from functools import wraps


def with_attempts(attempts, sleep_time):
    def _with_attempts(old_function):
        number_of_calls = 0

        @wraps(old_function)
        def new_function(*args, **kwargs):
            nonlocal number_of_calls
            number_of_calls += 1
            error = None
            for i in range(1, attempts + 1):
                try:
                    result = old_function(*args, **kwargs)
                    return result
                except Exception as er:
                    time.sleep(sleep_time)
                    error = er
                    print(f"Попытка {i} не удалась. Ошибка: {er}")

            raise error

        return new_function

    return _with_attempts
