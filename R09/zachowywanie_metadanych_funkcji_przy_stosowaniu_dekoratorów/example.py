import time
from functools import wraps

def timethis(func):
    '''
    Dekorator informujący o czasie wykonywania kodu
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

if __name__ == '__main__':
    @timethis
    def countdown(n:int):
        '''
        Odliczanie w dół
        '''
        while n > 0:
            n -= 1

    countdown(100000)
    print('Nazwa:', countdown.__name__)
    print('Łańcuch znaków z dokumentacją:', repr(countdown.__doc__))
    print('Uwagi:', countdown.__annotations__)
