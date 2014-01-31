# Dostęp do zmiennych z domknięcia

def sample():
    n = 0           
    # Domknięcie
    def func():
        print('n=', n)
    
    # Akcesory dla atrybutu n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Dołącanie akcesorów jako atrybutów funkcji
    func.get_n = get_n
    func.set_n = set_n
    return func

if __name__ == '__main__':
    f = sample()
    f()
    n= 0
    f.set_n(10)
    f()
    print(f.get_n())
