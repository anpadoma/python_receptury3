# Inna wersja. Tu atrybuty funkcji są używane bezpośrednio

from functools import wraps
import logging

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
            wrapper.log.log(wrapper.level, wrapper.logmsg)
            return func(*args, **kwargs)

        # Dołączanie modyfikowalnych atrybutów
        wrapper.level = level
        wrapper.logmsg = logmsg
        wrapper.log = log

        return wrapper
    return decorate

# Przykład zastosowania
@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    print(add(2, 3))

    # Zmiana rejestrowanego komunikatu
    add.logmsg = 'Wywołano funkcję add'
    print(add(2, 3))

    # Zmiana poziomu rejestrowania
    add.level = logging.WARNING
    print(add(2, 3))
