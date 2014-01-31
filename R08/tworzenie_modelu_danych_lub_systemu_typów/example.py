# Klasa bazowa. Wykorzystuje deskryptor do ustawiania wartości
class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        self.__dict__.update(opts)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

# Deskryptory wymuszające stosowanie określonych typów
class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Oczekiwano typu ' + str(self.expected_type))
        super().__set__(instance, value)

# Deskryptor do wymuszania wartości
class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Oczekiwano wartości >= 0')
        super().__set__(instance, value)

class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('Brak opcji size')
        self.size = opts['size']
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('Opcja size musi być < ' + str(self.size))
        super().__set__(instance, value)

class Integer(Typed):
    expected_type = int

class UnsignedInteger(Integer, Unsigned):
    pass

class Float(Typed):
    expected_type = float

class UnsignedFloat(Float, Unsigned):
    pass

class String(Typed):
    expected_type = str

class SizedString(String, MaxSized):
    pass

# Dekoratory klas do stosowania ograniczeń
def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls
    return decorate

# Metaklasa do sprawdzania typów
class checkedmeta(type):
    def __new__(cls, clsname, bases, methods):
        # Dołączanie nazw atrybutów do deskryptorów
        for key, value in methods.items():
            if isinstance(value, Descriptor):
                value.name = key
        return type.__new__(cls, clsname, bases, methods)

# Testowanie kodu
def test(s):
    print(s.name)
    s.shares = 75
    print(s.shares)
    try:
        s.shares = -10
    except ValueError as e:
        print(e)
    try:
        s.price = 'Dużo'
    except TypeError as e:
        print(e)

    try:
        s.name = 'ABRACADABRA'
    except ValueError as e:
        print(e)

# Różne przykłady:
if __name__ == '__main__':
    print("# --- Klasa z deskryptorami")
    class Stock:
        # Określanie ograniczeń
        name = SizedString('name',size=8)
        shares = UnsignedInteger('shares')
        price = UnsignedFloat('price')
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price

    s = Stock('ACME',50,91.1)
    test(s)

    print("# --- Klasa z dekoratorem klasy")
    @check_attributes(name=SizedString(size=8), 
                      shares=UnsignedInteger,
                      price=UnsignedFloat)
    class Stock:
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price

    s = Stock('ACME',50,91.1)
    test(s)

    print("# --- Klasa z metaklasą")
    class Stock(metaclass=checkedmeta):
        name   = SizedString(size=8)
        shares = UnsignedInteger()
        price  = UnsignedFloat()
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price

    s = Stock('ACME',50,91.1)
    test(s)
        
