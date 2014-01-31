# example.py
#
# Ustalanie wspólnych danych z dwóch słowników

a = {
   'x' : 1,
   'y' : 2,
   'z' : 3
}

b = {
   'w' : 10,
   'x' : 11,
   'y' : 2
}

print('Wspólne klucze:', a.keys() & b.keys())
print('Klucze z a, których nie ma w b:', a.keys() - b.keys())
print('Wspólne pary (klucz,wartość):', a.items() & b.items())

