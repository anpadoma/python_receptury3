from functools import wraps, partial
import logging

def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func

def logged(level, name=None, message=None):
    '''
	Dodawanie rejestrowania do funkcji. level to poziom
	rejestrowania, name to nazwa rejestratora, a message to
	rejestrowany komunikat. Jeśli nie określono argumentów name
	i message, używane są moduł i nazwa funkcji. 
    '''
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        # Dołączanie funkcji do ustawiania wartości
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper
    return decorate

# Przykład zastosowania
@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

# Zastosowanie wielu dekoratorów

import time
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return r
    return wrapper

@timethis
@logged(logging.DEBUG)
def countdown(n):
    while n > 0:
        n -= 1


@logged(logging.DEBUG)
@timethis
def countdown2(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    print(add(2, 3))

    # Zmiana rejestrowanego komunikatu
    add.set_message('Wywołano funkcję add')
    print(add(2, 3))

    # Zmiana poziomu rejestrowania
    add.set_level(logging.WARNING)
    print(add(2, 3))

    countdown(100000)
    countdown.set_level(logging.CRITICAL)
    countdown(100000)

    countdown2(100000)
    countdown2.set_level(logging.CRITICAL)
    countdown2(100000)
