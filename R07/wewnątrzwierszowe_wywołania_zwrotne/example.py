# Implementowanie wewnątrzwierszowych funkcji wywoływanych zwrotnie

# Przykładowa funkcja ilustrująca przepływ sterowania przy stosowaniu wywołań zwrotnych

def apply_async(func, args, *, callback):
    # Obliczanie wyniku
    result = func(*args)

    # Wywołanie zwrotne (z przekazanym wynikiem)
    callback(result)

# Wewnątrzwierszowe wywołanie zwrotne
from queue import Queue
from functools import wraps

class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args

def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break
    return wrapper

# Przykład zastosowania
def add(x, y):
    return x + y

@inlined_async
def test():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('Witaj', 'świecie'))
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print('Żegnaj')

if __name__ == '__main__':
    # Prosty test
    print('# --- Prosty test')
    test()

    print('# --- Test z modułem multiprocessing')
    import multiprocessing
    pool = multiprocessing.Pool()
    apply_async = pool.apply_async
    test()
