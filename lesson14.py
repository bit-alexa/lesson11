'''Task 1'''

def logger(func):
    def wrapper(*args, **kwargs):
        print('Task 1: ', func.__name__, 'called with ', *args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(4,5)

def func1():
    def func2():
        print('func2')
    return func2

'''Task2
Write a decorator that takes a list of stop words and replaces them with * inside the decorated function'''

def stop_words(words: list):
    def decor(f):
        def wrapper(*args, **kwargs):
            res = f(*args, **kwargs)
            for i in words:
                res = res.replace(i, '*')
            return res
        return wrapper
    return decor


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

'''Task 3'''


def arg_rules(type_: type, max_length: int, contains: list):
    def decor(f):
        def wrapper(arg):
            if type(arg) != type_:
                print(f'Argument must be string, not {type(arg)}')
                return False
            elif len(arg) > max_length:
                print(f'Argument must be up to {max_length} characters')
                return False
            elif False in [True for i in contains if i in arg]:
                print(f'Argument must not have this: {contains}')
                return False
            else:
                return f(arg)

        return wrapper

    return decor


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
