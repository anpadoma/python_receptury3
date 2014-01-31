# Pomijanie dekoratora

from functools import wraps

def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Dekorator 1')
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Dekorator 2')
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def add(x, y):
    return x + y

# Wywołanie funkcji za pomocą nakładki
print(add(2,3))

# Wywołanie pierwotnej funkcji
print(add.__wrapped__(2,3))
