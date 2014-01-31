def lazyproperty(func):
    name = '_lazy_' + func.__name__
    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value
    return lazy
        
if __name__ == '__main__':
    import math
    class Circle:
        def __init__(self, radius):
            self.radius = radius

        @lazyproperty
        def area(self):
            print('Obliczanie powierzchni')
            return math.pi * self.radius ** 2

        @lazyproperty
        def perimeter(self):
            print('Obliczanie obwodu')
            return 2 * math.pi * self.radius

