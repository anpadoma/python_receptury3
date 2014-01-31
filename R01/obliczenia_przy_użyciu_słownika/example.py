# example.py
#
# Przykładowe obliczenia z wykorzystaniem słownika

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

# Znajduje cenę minimalną i maksymalną
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

print('Minimalna cena:', min_price)
print('Maksymalna cena:', max_price)

print('Posortowane ceny:')
prices_sorted = sorted(zip(prices.values(), prices.keys()))
for price, name in prices_sorted:
    print('    ', name, price)


