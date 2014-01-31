# Ten przykład dotyczy przenoszenia dodatkowego stanu przy użyciu
# wywoływanych zwrotnie funkcji. W ramach testów ten bardzo prosty
# kod symuluje typowy dla wywołań zwrotnych przepływ sterowania.

def apply_async(func, args, *, callback):
    # Obliczanie wyniku
    result = func(*args)

    # Wywołanie zwrotne (z przekazanym wynikiem)
    callback(result)

# Prosta funkcja używana w testach
def add(x, y):
    return x + y

# (a) Proste przykładowe wywołanie zwrotne

print('# --- Prosty przykład')

def print_result(result):
    print("Pobrano:", result)

apply_async(add, (2, 3), callback=print_result)
apply_async(add, ('Witaj', 'świecie'), callback=print_result)

# (b) Używanie wiązanej metody

print('# --- Używanie wiązanej metody')

class ResultHandler:
    def __init__(self):
        self.sequence = 0
    def handler(self, result):
        self.sequence += 1
        print('[{}] Pobrano: {}'.format(self.sequence, result))

r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)
apply_async(add, ('Witaj', 'świecie'), callback=r.handler)

# (c) Używanie domknięć

print('# --- Używanie domknięcia')

def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Pobrano: {}'.format(sequence, result))
    return handler

handler = make_handler()
apply_async(add, (2, 3), callback=handler)
apply_async(add, ('Witaj', 'świecie'), callback=handler)


# (d) Używanie współprogramu

print('# --- Używanie współprogramu')

def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Pobrano: {}'.format(sequence, result))

handler = make_handler()
next(handler)    # Przechodzenie do polecenia yield

apply_async(add, (2, 3), callback=handler.send)
apply_async(add, ('Witaj', 'świecie'), callback=handler.send)

# (e) Zastosowanie funkcji częściowych

print('# --- Używanie funkcji częściowych')

class SequenceNo:
    def __init__(self):
        self.sequence = 0

def handler(result, seq):
    seq.sequence += 1
    print('[{}] Pobrano: {}'.format(seq.sequence, result))

seq = SequenceNo()
from functools import partial

apply_async(add, (2, 3), callback=partial(handler, seq=seq))
apply_async(add, ('Witaj', 'świecie'), callback=partial(handler, seq=seq))


