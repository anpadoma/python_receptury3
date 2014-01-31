# Iterowanie po wierszach pliku z dodatkowym atrybutem lineno
def parse_data(filename):
    with open(filename, 'rt') as f:
         for lineno, line in enumerate(f, 1):
             fields = line.split()
             try:
                 count = int(fields[1])
             except ValueError as e:
                 print('Wiersz {}: Błąd parsowania: {}'.format(lineno, e))

parse_data('sample.dat')
