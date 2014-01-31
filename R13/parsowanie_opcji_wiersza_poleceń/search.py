# search.py
'''
Fikcyjne narzędzie wiersza poleceń służące do przeszukiwania
kolekcji plików pod kątem wzorców.
'''
import argparse
parser = argparse.ArgumentParser(description='Wyszukuje pliki')

parser.add_argument(dest='filenames',metavar='filename', nargs='*')

parser.add_argument('-p', '--pat',metavar='pattern', required=True,
                    dest='patterns', action='append',
                    help='Szukany wzorzec')

parser.add_argument('-v', dest='verbose', action='store_true', 
                    help='Tryb pełny')

parser.add_argument('-o', dest='outfile', action='store',
                    help='Plik wyjściowy')

parser.add_argument('--speed', dest='speed', action='store',
                    choices={'slow','fast'}, default='slow',
                    help='Szybkość wyszukiwania')

args = parser.parse_args()

# Wyświetla otrzymane argumenty
print(args.filenames)
print(args.patterns)
print(args.verbose)
print(args.outfile)
print(args.speed)
