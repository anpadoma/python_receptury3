# Skomplikowany problem inicjowania związany z wielodziedziczeniem.
# Z użyciem funkcji super()

class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')

class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')

class C(A,B):
    def __init__(self):
        super().__init__()     # Tylko jedno wywołanie super()
        print('C.__init__')

if __name__ == '__main__':
    # Zauważ, że każda klasa jest inicjowana tylko raz
    c = C()
