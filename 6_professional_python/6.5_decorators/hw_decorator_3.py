import os.path
import types
import datetime


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            time_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            funcname = old_function.__name__
            args_ = ', '.join([repr(arg) for arg in args])
            kwargs_ = ', '.join([f'{key}={value}' for key, value in kwargs.items()])
            if args_ and kwargs_:
                arguments = f'{args_}, {kwargs_}'
            elif args_:
                arguments = f'{args_}'
            elif kwargs_:
                arguments = f'{kwargs_}'
            else:
                arguments = f'Аргументы отсутствуют'

            result = list(old_function(*args, **kwargs))

            log_ = f'В {time_date} была вызвана функция {funcname} с аргументами {arguments}. Результат выполнения функции {result}'
            with open(path, 'a') as f:
                f.write(log_ + '\n')

            return result

        return new_function

    return __logger




def test_4():
    path='log_gen.log'
    if os.path.exists(path):
        os.remove(path)
    @logger(path)
    def flat_generator(list_of_list):
        for list_ in list_of_list:
            if isinstance(list_, list):
                for element in flat_generator(list_):
                    yield element
            else:
                yield list_

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    flat_list = flat_generator(list_of_lists_2)

if __name__ == '__main__':
    test_4()