# example.py
#
# Przykładowy prosty rekurencyjny parser zstępujący

import re
import collections

# Specyfikacja tokenów
NUM    = r'(?P<NUM>\d+)'
PLUS   = r'(?P<PLUS>\+)'
MINUS  = r'(?P<MINUS>-)'
TIMES  = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS     = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES, 
                                  DIVIDE, LPAREN, RPAREN, WS]))

# Mechanizm podziału na tokeny
Token = collections.namedtuple('Token', ['type','value'])

def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok

# Parser 
class ExpressionEvaluator:
    '''
    Rekurencyjny parser zstępujący. Każda metoda obsługuje jedną
    regułę gramatyki. Metoda ._accept() służy do testowania i 
    akceptowania aktualnie "podglądanego" tokenu. Metoda ._expect()
    pozwala dokładnie dopasować i odrzucić następny token z danych wejściowych
    (jeśli token nie pasuje do wzorca, zgłaszany jest wyjątek SyntaxError).
    '''

    def parse(self,text):
        self.tokens = generate_tokens(text)
        self.tok = None             # Ostatni pobrany symbol 
        self.nexttok = None         # Następny symbol przekształcany na token
        self._advance()             # Wczytywanie pierwszego "podglądanego" tokenu
        return self.expr()

    def _advance(self):
        'Przejście do następnego tokenu'
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

    def _accept(self,toktype):
        'Testowanie następnego tokenu i pobieranie go, jeśli pasuje do typu toktype'
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

    def _expect(self,toktype):
        'Pobieranie następnego tokenu, jeśli pasuje do typu toktype, lub zgłaszanie błędu SyntaxError'
        if not self._accept(toktype):
            raise SyntaxError('Oczekiwano ' + toktype)

    # Zasady gramatyki

    def expr(self):
        "expression ::= term { ('+'|'-') term }*"

        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval += right
            elif op == 'MINUS':
                exprval -= right
        return exprval
    
    def term(self):
        "term ::= factor { ('*'|'/') factor }*"

        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval *= right
            elif op == 'DIVIDE':
                termval /= right
        return termval

    def factor(self):
        "factor ::= NUM | ( expr )"

        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Oczekiwano tokenu typu NUMBER lub LPAREN')

if __name__ == '__main__':
    e = ExpressionEvaluator()
    print(e.parse('2'))
    print(e.parse('2 + 3'))
    print(e.parse('2 + 3 * 4'))
    print(e.parse('2 + (3 + 4) * 5'))

# Przykład ilustrujący tworzenie drzew

class ExpressionTreeBuilder(ExpressionEvaluator):
    def expr(self):
        "expression ::= term { ('+'|'-') term }"

        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval = ('+', exprval, right)
            elif op == 'MINUS':
                exprval = ('-', exprval, right)
        return exprval
    
    def term(self):
        "term ::= factor { ('*'|'/') factor }"

        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval = ('*', termval, right)
            elif op == 'DIVIDE':
                termval = ('/', termval, right)
        return termval

    def factor(self):
        'factor ::= NUM | ( expr )'

        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Oczekiwano tokenu typu NUMBER lub LPAREN')

if __name__ == '__main__':
    e = ExpressionTreeBuilder()
    print(e.parse('2 + 3'))
    print(e.parse('2 + 3 * 4'))
    print(e.parse('2 + (3 + 4) * 5'))
    print(e.parse('2 + 3 + 4'))
