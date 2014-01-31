# Wczytywanie plików tekstowych z użyciem różnych opcji
#
# Plik sample.txt zawiera tekst w formacie UTF-8 z zakończeniami 
# wierszy typowymi dla systemu Windows (\r\n).

# (a) Wczytywanie prostego pliku tekstowego (domyślny format UTF-8)

print("Wczytywanie prostego pliku tekstowego (UTF-8)")
with open('sample.txt', 'rt') as f:
    for line in f:
        print(repr(line))

# (b) Wczytywanie pliku tekstowego bez uniwersalnych znaków nowego wiersza
print("Wczytywanie pliku tekstowego bez uniwersalnych znaków nowego wiersza")
with open('sample.txt', 'rt', newline='') as f:
    for line in f:
        print(repr(line))

# (c) Wczytywanie pliku tekstowego jako pliku ASCII; błędne znaki są zastępowane
print("Wczytywanie danych jako tekstu ASCII (błędne znaki są zastępowane)")
with open('sample.txt', 'rt', encoding='ascii', errors='replace') as f:
    for line in f:
        print(repr(line))

# (d) Wczytywanie pliku tekstowego jako pliku ASCII; błędne znaki są ignorowane
print("Wczytywanie danych jako tekstu ASCII (błędne znaki są ignorowane)")
with open('sample.txt', 'rt', encoding='ascii', errors='ignore') as f:
    for line in f:
        print(repr(line))

