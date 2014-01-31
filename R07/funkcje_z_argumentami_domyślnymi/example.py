# Przykładowe funkcje z argumentami domyślnymi 

# (a) Zagrożenia związane ze stosowaniem modyfikowalnych argumentów domyślnych

def spam(b=[]):
    return b

a = spam()
print(a)
a.append(1)
a.append(2)
b = spam()
print(b)       #  Dokładnie obserwuj wyniki
print('-'*10)

# (b) Lepsze rozwiązanie z modyfikowalnymi argumentami domyślnymi
def spam(b=None):
    if b is None:
        b = []
    return b

a = spam()
print(a)
a.append(1)
a.append(2)
b = spam()
print(b)
print('-'*10)

# (c) Sprawdzanie, czy podano argument czy nie

_no_value = object()
def spam(b=_no_value):
    if b is _no_value:
        print("Nie podano wartości argumentu b")
    else:
        print("b=", b)

spam()
spam(None)
spam(0)
spam([])
