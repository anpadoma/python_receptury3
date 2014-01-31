# example.py
#
# Przykład ilustrujący łączenie słowników w obiekt typu ChainMap

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

# (a) Prosty przykład ilustrujący łączenie
from collections import ChainMap
c = ChainMap(a,b)
print(c['x'])      # Zwraca 1  (z a)
print(c['y'])      # Zwraca 2  (z b)
print(c['z'])      # Zwraca 3  (z a)

# Wyświetlanie typowych atrybutów
print('len(c):', len(c))
print('c.keys():', list(c.keys()))
print('c.values():', list(c.values()))

# Modyfikowanie wartości
c['z'] = 10
c['w'] = 40
del c['x']
print("a:", a)


# Tworzenie kilku poziomów odwzorowań (przypomina działanie zasięgu)
values = ChainMap()
values['x'] = 1

# Dodawanie nowego odwzorowania
values = values.new_child()
values['x'] = 2

# Dodawanie nowego odwzorowania
values = values.new_child()
values['x'] = 3

print(values)
print(values['x'])

# Usuwanie ostatniego odwzorowania
values = values.parents
print(values)
print(values['x'])

# Usuwanie ostatniego odwzorowania
values = values.parents
print(values)
print(values['x'])

