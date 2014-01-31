# Przykład oparty na module array
import sample
import array
a = array.array('d',[1,-3,4,7,2,0])
print(a)
sample.clip(a,1,4,a)
print(a)

# Przykład oparty na bibliotece numpy
import numpy
b = numpy.random.uniform(-10,10,size=1000000)
print(b)
c = numpy.zeros_like(b)
print(c)
sample.clip(b,-5,5,c)
print(c)
print(min(c))
print(max(c))

# Pomiary testowe
from timeit import timeit
print('numpy.clip')
print(timeit('numpy.clip(b,-5,5,c)', 'from __main__ import b,c,numpy', number=1000))
print('sample.clip')
print(timeit('sample.clip(b,-5,5,c)', 'from __main__ import b,c,sample', number=1000))

print('sample.clip_fast')
print(timeit('sample.clip_fast(b,-5,5,c)', 'from __main__ import b,c,sample', number=1000))

# Test dla tablic dwuwymiarowych
d = numpy.random.uniform(-10,10,size=(1000,1000))
print(d)
sample.clip2d(d, -5, 5, d)
print(d)
