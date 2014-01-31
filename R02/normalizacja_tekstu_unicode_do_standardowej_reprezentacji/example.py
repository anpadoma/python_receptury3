# example.py
#
# Normalizacja tekstu Unicode

# Dwa łańcuchy znaków
s1 = 'Papryczki Jalape\u00f1o'
s2 = 'Papryczki Jalapen\u0303o'

# (a) Wyświetlanie łańcuchów (zwykle wyglądają identycznie)
print(s1)
print(s2)

# (b) Sprawdzanie identyczności i długości
print('s1 == s2', s1 == s2)
print(len(s1), len(s2))

# (c) Te same testy po normalizacji
import unicodedata

n_s1 = unicodedata.normalize('NFC', s1)
n_s2 = unicodedata.normalize('NFC', s2)

print('n_s1 == n_s2', n_s1 == n_s2)
print(len(n_s1), len(n_s2))

# (d) Normalizacja do postaci ze znakami łączonymi i usuwanie akcentów
t1 = unicodedata.normalize('NFD', s1)
print(''.join(c for c in t1 if not unicodedata.combining(c)))
