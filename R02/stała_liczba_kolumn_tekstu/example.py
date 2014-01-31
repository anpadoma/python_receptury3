# example.py
#
# Zmiana formatowania tekstu w celu uzyskania innej liczby kolumn

# Długi łańcuch znaków
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

import textwrap

print(textwrap.fill(s, 70))
print()

print(textwrap.fill(s, 40))
print()

print(textwrap.fill(s, 40, initial_indent='    '))
print()

print(textwrap.fill(s, 40, subsequent_indent='    '))
print()

