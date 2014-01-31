# Zapisywanie nieprzetworzonych bajtów w pliku otwartym w trybie tekstowym

import sys

# Łańcuch bajtów
data = b'Witaj, Polsko\n'

# Zapisywanie danych do atrybutu buffer (z pominięciem kodowania)
sys.stdout.buffer.write(data)
