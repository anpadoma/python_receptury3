# namelower.py
import ast
import inspect

# Klasa "odwiedzająca" węzły, która przekształca globalnie 
# dostępne nazwy w ciele funkcji na zmienne lokalne
class NameLower(ast.NodeVisitor):
    def __init__(self, lowered_names):
        self.lowered_names = lowered_names

    def visit_FunctionDef(self, node):
        # Kompilowanie przypisań w celu zmiany zasięgu stałych
        code = '__globals = globals()\n'
        code += '\n'.join("{0} = __globals['{0}']".format(name)
                          for name in self.lowered_names)

        code_ast = ast.parse(code, mode='exec')

        # Wstawianie nowych poleceń do ciała funkcji
        node.body[:0] = code_ast.body

        # Zapisywanie obiektu z funkcją
        self.func = node

# Dekorator przekształcający nazwy globalne na lokalne
def lower_names(*namelist):
    def lower(func):
        srclines = inspect.getsource(func).splitlines()
        # Pomijanie wierszy kodu źródłowego do dekoratora @lower_names
        for n, line in enumerate(srclines):
            if '@lower_names' in line:
                break

        src = '\n'.join(srclines[n+1:])
        # Sztuczka umożliwająca radzenie sobie z wcięciami w kodzie
        if src.startswith((' ','\t')):
            src = 'if 1:\n' + src
        top = ast.parse(src, mode='exec')

        # Przekształcanie drzewa składniowego 
        cl = NameLower(namelist)
        cl.visit(top)

        # Wykonywanie kodu z przekształconego drzewa składniowego
        temp = {}
        exec(compile(top,'','exec'), temp, temp)

		# Pobieranie zmodyfikowanego obiektu z kodem
        func.__code__ = temp[func.__name__].__code__
        return func
    return lower

# Przykład zastosowania
INCR = 1

def countdown1(n):
    while n > 0:
        n -= INCR

@lower_names('INCR')
def countdown2(n):
    while n > 0:
        n -= INCR

if __name__ == '__main__':
    import time
    print('Test wydajności')

    start = time.time()
    countdown1(100000000)
    end = time.time()
    print('countdown1:', end-start)

    start = time.time()
    countdown2(100000000)
    end = time.time()
    print('countdown2:', end-start)

