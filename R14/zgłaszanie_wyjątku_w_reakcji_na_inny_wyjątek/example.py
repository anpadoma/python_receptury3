# Różne sposoby zgłaszania wyjątków w łańcuchu

# Przykład 1. Bezpośrednie tworzenie łańcucha. Należy stosować, gdy celem jest
# zgłoszenie nowego wyjątku w reakcji na wystąpienie innego

def example1():
    try:
        int('Brak')
    except ValueError as e:
        raise RuntimeError('Błąd parsowania') from e

# Przykład 2. Niejawne tworzenie łańcucha. Ma miejsce, gdy wystąpi
# nieoczekiwany wyjątek w bloku except.

def example2():
    try:
        int('Brak')
    except ValueError as e:
        print('Niepowodzenie. Powód:', err)   # Celowo wywołany błąd

# Przykład 3. Usuwanie wcześniej zgłoszonych wyjątków
def example3():
    try:
        int('Brak')
    except ValueError as e:
        raise RuntimeError('Błąd parsowania') from None

if __name__ == '__main__':
    import traceback
    print('****** BEZPOŚREDNIO TWORZONY ŁAŃCUCH WYJĄTKÓW ******')
    try:
        example1()
    except Exception:
        traceback.print_exc()

    print()
    print('****** NIEJAWNIE TWORZONY ŁAŃCUCH WYJĄTKÓW ******')
    try:
        example2()
    except Exception:
        traceback.print_exc()

    print()
    print('****** REZYGNACJA Z ŁAŃCUCHA *******')
    try:
        example3()
    except Exception:
        traceback.print_exc()


