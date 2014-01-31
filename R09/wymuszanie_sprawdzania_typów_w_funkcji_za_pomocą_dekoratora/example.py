from inspect import signature
from functools import wraps

def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # Jeśli kod działa w trybie zaoptymalizowanym, nie należy sprawdzać typów
        if not __debug__:
            return func
			
		# Odwzorowanie nazw argumentów funkcji na typy
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Wymuszanie typów przekazanych argumentów
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} musi być typu {}'.format(name, bound_types[name])
                            )
            return func(*args, **kwargs)
        return wrapper
    return decorate

# Przykłady

@typeassert(int, int)
def add(x, y):
    return x + y

@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)

if __name__ == '__main__':
    print(add(2,3))
    try:
        add(2, 'Witaj')
    except TypeError as e:
        print(e)

    spam(1, 2, 3)
    spam(1, 'Witaj', 3)
    try:
        spam(1, 'Witaj', 'świecie')
    except TypeError as e:
        print(e)

