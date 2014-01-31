# example.py
#
# Proste podstawianie tekstu z wykorzystaniem wyrażeń regularnych

import re

# Przykładowy tekst
text = 'Dzisiaj jest 11/27/2012. Konferencja PyCon zaczyna się 3/13/2013.'

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

# (a) Proste podstawianie
print(datepat.sub(r'\3-\1-\2', text))

# (b) Funkcja zastępująca tekst
from calendar import month_abbr

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

print(datepat.sub(change_date, text))
