import ast

class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loaded = set()
        self.stored = set()
        self.deleted = set()
    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.loaded.add(node.id)
        elif isinstance(node.ctx, ast.Store):
            self.stored.add(node.id)
        elif isinstance(node.ctx, ast.Del):
            self.deleted.add(node.id)

# Przykład zastosowania
if __name__ == '__main__':
    # Kod w Pythonie
    code = '''
for i in range(10): 
    print(i)
del i
'''
    # Parsowanie do drzewa składniowego
    top = ast.parse(code, mode='exec')

    # Przekazywanie drzewa składniowego do analizy używanych nazw
    c = CodeAnalyzer()
    c.visit(top)
    print('Wczytano:', c.loaded)
    print('Zapisano:', c.stored)
    print('Usunięto:', c.deleted)
