import os
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

            result = old_function(*args, **kwargs)

            log_ = f'В {time_date} была вызвана функция {funcname} с аргументами {arguments}. Результат выполнения функции {result}'
            with open(path, 'a') as f:
                f.write(log_ + '\n')

            return result

        return new_function

    return __logger

def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_2()