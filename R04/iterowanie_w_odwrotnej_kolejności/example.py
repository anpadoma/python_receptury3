# Przykładowy obiekt z iteratorami przechodzącymi w obu kierunkach

class Countdown:
    def __init__(self, start):
        self.start = start

    # Iterator przechodzący do przodu
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Iterator przechodzący do tyłu
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

c = Countdown(5)
print("Do przodu:")
for x in c:
    print(x)

print("Do tyłu:")
for x in reversed(c):
    print(x)
