# example.py
#
# Łączenie tekstu za pomocą generatorów

def sample():
    yield "Co"
    yield "stolica"
    yield "to"
    yield "stolica"

# (a) Prosty operator join
text = ''.join(sample())
print(text)

# (b) Przekierowywanie porcji tekstu do strumienia wyjścia
import sys
for part in sample():
    sys.stdout.write(part)
sys.stdout.write('\n')

# (c) Łączenie porcji tekstu w buforach i większych operacjach wejścia-wyjścia
def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)

for part in combine(sample(), 32768):
    sys.stdout.write(part)
sys.stdout.write('\n')


