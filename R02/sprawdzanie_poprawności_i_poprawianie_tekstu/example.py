# example.py
#
# Podchwytliwe problemy ze sprawdzaniem poprawności

# Skomplikowany łańcuch znaków
s = 'p\xfdt\u0125\xf6\xf1\x0cis\tawesome\r\n'
print(s)

# (a) Modyfikowanie odstępów
remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None      # Usuwany
}

a = s.translate(remap)
print('Zmodyfikowano odstępy:', a)

# (b) Usuwanie wszystkich znaków łączonych
import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)
c = b.translate(cmb_chrs)
print('Usunięto akcenty:', c)

# (c) Usuwanie akcentów z wykorzystaniem operacji wejścia-wyjścia
d = b.encode('ascii','ignore').decode('ascii')
print('Akcenty usunięte w operacjach wejścia-wyjścia:', d)
