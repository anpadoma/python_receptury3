# example.py
import sample

def foo():
    print('Przed zamknięciem')
    sample.die()

def bar():
    print('Przed wywołaniem funkcji, która powoduje zamknięcie')
    foo()

def spam():
    print('Przed wywołaniem funkcji, która wywołuje funkcję powodującą zamknięcie')
    bar()

if __name__ == '__main__':
    import faulthandler
    faulthandler.enable()
    spam()

