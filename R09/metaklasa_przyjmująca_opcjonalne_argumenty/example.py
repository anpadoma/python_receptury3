# Przykładowa metaklasa przyjmująca opcjonalne argumenty

class MyMeta(type):
    # Opcjonalne
    @classmethod
    def __prepare__(cls, name, bases, *, debug=False, synchronize=False):
        # Niestandardowe przetwarzanie
        return super().__prepare__(name, bases)

    # Wymagane
    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        # Niestandardowe przetwarzanie
        return super().__new__(cls, name, bases, ns)
        
    def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
        # Niestandardowe przetwarzanie
        super().__init__(name, bases, ns)

# Przykłady
class A(metaclass=MyMeta, debug=True, synchronize=True):
    pass

class B(metaclass=MyMeta):
    pass

class C(metaclass=MyMeta, synchronize=True):
    pass

    

