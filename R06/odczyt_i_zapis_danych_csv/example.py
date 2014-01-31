# example.py
#
# Różne przykłady wczytywania zawartości plików CSV

import csv

# (a) Wczytywanie danych jako krotek

print('Wczytywanie danych jako krotek:')
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Przetwarzanie wiersza
        print('    ', row)

# (b) Wczytywanie danych jako krotek nazwanych

print('Wczytywanie danych jako krotek nazwanych')
from collections import namedtuple
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    Row = namedtuple('Row', next(f_csv))
    for r in f_csv:
        row = Row(*r)
        # Przetwarzanie wiersza
        print('    ', row)


# (c) Wczytywanie danych jako słowników

print('Wczytywanie danych jako słowników')
with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        # Przetwarzanie wiersza
        print('    ', row)

# (d) Wczytywanie danych do krotek z konwersją typu

print('Wczytywanie danych do krotek z konwersją typu')

col_types = [str, float, str, str, float, int]
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Przekształcanie elementów wiersza
        row = tuple(convert(value) for convert, value in zip(col_types, row))
        print(row)

# (e) Przekształcanie wybranych pól słownika

print('Wczytywanie danych do słownika z konwersją typu')

field_types = [ ('Price', float),
                ('Change', float),
                ('Volume', int) ]

with open('stocks.csv') as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key])) 
                   for key, conversion in field_types)
        print(row)

        



