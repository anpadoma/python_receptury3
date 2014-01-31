# example.py
#
# Przykład ilustrujący wykorzystanie generatorów jako argumentów

import os
files = os.listdir(os.path.expanduser('~'))
if any(name.endswith('.py') for name in files):
    print('Znaleziono pliki Pythona!')
else:
    print('Niestety, nie ma plików Pythona')

# Zwracanie krotki jako danych w formacie CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Redukowanie danych na podstawie pól ze struktury danych
portfolio = [
   {'name':'GOOG', 'shares': 50},
   {'name':'YHOO', 'shares': 75},
   {'name':'AOL', 'shares': 20},
   {'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
