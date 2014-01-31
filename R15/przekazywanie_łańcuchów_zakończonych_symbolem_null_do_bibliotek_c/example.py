import sample
import sys

sample.print_chars(b'witaj, Polsko')

s = 'Papryczka Jalape\u00f1o'
print(sys.getsizeof(s))
sample.print_chars_str(s)
print(sys.getsizeof(s))
del s

s = 'Papryczka Jalape\u00f1o'
print(sys.getsizeof(s))
sample.print_chars_str_alt(s)
print(sys.getsizeof(s))
