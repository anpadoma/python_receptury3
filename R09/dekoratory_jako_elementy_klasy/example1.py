from functools import wraps

class A:
    # Dekorator jako metoda egzemplarza
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Dekorator 1')
            return func(*args, **kwargs)
        return wrapper

    # Dekorator jako metoda klasy
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Dekorator 2')
            return func(*args, **kwargs)
        return wrapper

# Przykład
# Jako metoda egzemplarza
a = A()

@a.decorator1
def spam():
    pass

# Jako metoda klasy
@A.decorator2
def grok():
    pass

spam()
grok()
