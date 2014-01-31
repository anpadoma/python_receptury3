# Funkcje przyjmujące argumenty podawane tylko za pomocą słów kluczowych

# Prosty argument podawany tylko za pomocą słowa kluczowego
def recv(maxsize, *, block=True):
    print(maxsize, block)

recv(8192, block=False)        # Poprawnie
try:
    recv(8192, False)          # Błąd
except TypeError as e:
    print(e)

# Dodawanie argumentów podawanych tylko za pomocą słów kluczowych do
# funkcji przyjmującej argumenty *args
def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

print(minimum(1, 5, 2, -5, 10))
print(minimum(1, 5, 2, -5, 10, clip=0))
