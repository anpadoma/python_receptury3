# Różne sposoby filtrowania danych

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# Tylko wartości dodatnie
pos = [n for n in mylist if n > 0]
print(pos)

# Tylko wartości ujemne
neg = [n for n in mylist if n < 0]
print(neg)

# Wartości ujemne są zastępowane zerami
neg_clip = [n if n > 0 else 0 for n in mylist]
print(neg_clip)

# Wartości dodatnie są zastępowane zerami
pos_clip = [n if n < 0 else 0 for n in mylist]
print(pos_clip)

# Przykład ilustrujący kompresję

addresses = [
    '5412 N CLARK',
    '5148 N CLARK', 
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

more5 = [ n > 5 for n in counts ]
a = list(compress(addresses, more5))
print(a)



