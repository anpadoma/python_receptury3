# Iterowanie po rekordach o stałej wielkości
#
# Plik 'data.bin' zawiera rekordy o długości 32-bajtów, składające się
# z 4-cyfrowej liczby, po której następuje 28-bajtowy łańcuch znaków.

from functools import partial
RECORD_SIZE = 32

with open('data.bin', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)

