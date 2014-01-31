class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()      # Wywołanie funkcji spam() z klasy bazowej

if __name__ == '__main__':
    b = B()
    b.spam()
