# plyexample.py
#
# Parsowanie z wykorzystaniem pakietu PLY

from ply.lex import lex
from ply.yacc import yacc

# Lista tokenów
tokens = [ 'NUM', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN' ]

# Ignorowane znaki

t_ignore = ' \t\n'

# Specyfikacje tokenów (w postaci wyrażeń regularnych)
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Funkcje do przetwarzania tokenów
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Obsługa błędów
def t_error(t):
    print('Nieprawidłowy znak: {!r}'.format(t.value[0]))
    t.skip(1)

# Tworzenie leksera
lexer = lex()

# Zasady gramatyki i funkcje obsługi
def p_expr(p):
    '''
    expr : expr PLUS term
         | expr MINUS term
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]

def p_expr_term(p):
    '''
    expr : term
    '''
    p[0] = p[1]

def p_term(p):
    '''
    term : term TIMES factor
         | term DIVIDE factor
    '''
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_term_factor(p):
    '''
    term : factor
    '''
    p[0] = p[1]

def p_factor(p):
    '''
    factor : NUM
    '''
    p[0] = p[1]

def p_factor_group(p):
    '''
    factor : LPAREN expr RPAREN
    '''
    p[0] = p[2]

def p_error(p):
    print('Błąd składni')

parser = yacc()

if __name__ == '__main__':
    print(parser.parse('2'))
    print(parser.parse('2+3'))
    print(parser.parse('2+(3+4)*5'))
