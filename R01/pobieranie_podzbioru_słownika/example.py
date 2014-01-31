# Pobieranie podzbioru słownika
from pprint import pprint

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

# Tworzenie słownika z cenami przekraczającymi 200
p1 = { key:value for key, value in prices.items() if value > 200 }

print("Wczystkie ceny powyżej 200")
pprint(p1)

# Tworzenie słownika z akcjami firm technologicznych
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key:value for key,value in prices.items() if key in tech_names }

print("Wszystkie akcje firm technologicznych")
pprint(p2)
