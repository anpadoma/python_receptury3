# example.py
#
# Sortowanie listy słowników na podstawie wspólnych kluczy

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

from pprint import pprint

print("Posortowane według pola fname:")
pprint(rows_by_fname)

print("Posortowane według pola uid:")
pprint(rows_by_uid)

rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print("Posortowane według pól lname,fname:")
pprint(rows_by_lfname)
