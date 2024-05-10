from functools import wraps


def decorator_template(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        print("Код до выполнения функции")
        result = old_function(*args, **kwargs)
        print("Код, который сработал после выполнения функции")

        return result

    return new_function


def parametrized_decorator_template(param1, param2):
    def decorator_template(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            print(f"Я могу использовать {param1=} и {param2=}")
            print("Код до выполнения функции")
            result = old_function(*args, **kwargs)
            print("Код, который сработал после выполнения функции")

            return result

        return new_function

    return decorator_template
