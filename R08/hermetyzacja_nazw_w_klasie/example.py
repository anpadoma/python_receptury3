# Przykład zastosowania nazw metod z członem __ do 
# tworzenia metod, których nie można przesłonić

class B:
    def __init__(self):
        self.__private = 0
    def __private_method(self):
        print('B.__private_method', self.__private)

    def public_method(self):
        self.__private_method()

class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1      # Nie przesłania metody override B.__private
    # Nie przesłania metody B.__private_method()
    def __private_method(self):
        print('C.__private_method')

c = C()
c.public_method()

