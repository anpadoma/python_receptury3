# example.py
#
# Podstawianie wartości za zmienne w łańcuchach znaków

# Klasa przeprowadzająca bezpieczne podstawianie
class safesub(dict):
    def __missing__(self, key):
        return '{%s}' % key

s = '{name} ma {n} wiadomości.'

# (a) Proste podstawianie
name = 'Gucio'
n = 37

print(s.format_map(vars()))

# (b) Bezpieczne podstawianie przy brakujących wartościach
del n
print(s.format_map(safesub(vars())))

# (c) Bezpieczne podstawianie plus sztuczka z ramką
n = 37
import sys
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

print(sub('Witaj, {name}'))
print(sub('{name} ma {n} wiadomości'))
print(sub('Twój ulubiony kolor to {color}'))
