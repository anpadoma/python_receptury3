# example.py
#
# Podział łańcuchów znaków według różnych ograniczników z wykorzystaniem wyrażeń regularnych

import re

line = 'asdf fjdk; afed, fjek,asdf,      foo'

# (a) Podział według odstępu, przecinka i średnika
parts = re.split(r'[;,\s]\s*', line)
print(parts)

# (b) Podział przy użyciu grupy przechwytującej
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

# (c) Odtwarzanie łańcucha znaków na podstawie zmiennej fields
values = fields[::2]
delimiters = fields[1::2]
delimiters.append('')
print('value =', values)
print('delimiters =', delimiters)
newline = ''.join(v+d for v,d in zip(values, delimiters))
print('newline =', newline)

# (d) Podział przy użyciu grupy nieprzechwytującej
parts = re.split(r'(?:,|;|\s)\s*', line)
print(parts)

