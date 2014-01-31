from functools import wraps
import logging

def logged(level, name=None, message=None):
    '''
	Dodawanie rejestrowania do funkcji. level to poziom
	rejestrowania, name to nazwa rejestratora, a message
	to rejestrowany komunikat. Jeśli nie podano argumentów
	name i message, domyślnie używane są moduł i nazwa funkcji.	
    '''
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

# Przykłąd zastosowania
@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    print(add(2,3))
    spam()
