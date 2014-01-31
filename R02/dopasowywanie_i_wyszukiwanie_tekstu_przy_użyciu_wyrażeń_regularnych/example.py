# example.py
#
# Proste dopasowywanie wyrażeń regularnych

import re

# Przykładowy tekst
text = 'Dzisiaj jest 11/27/2012. Konferencja PyCon rozpoczyna się 3/13/2013.'

# (a) Wyszukiwanie wszystkich pasujących dat
datepat = re.compile(r'\d+/\d+/\d+')
print(datepat.findall(text))

# (b) Wyszukiwanie wszystkich pasujących dat z wykorzystaniem grup przechwytujących
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

# (c) Wyszukiwanie iteracyjne
for m in datepat.finditer(text):
    print(m.groups())


