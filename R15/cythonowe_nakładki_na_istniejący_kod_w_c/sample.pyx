# sample.pyx

# Importowanie niskopoziomowych deklaracji z języka C
cimport csample

# Importowanie funkcji z Pythona i biblioteki stdlib języka C
from cpython.pycapsule cimport *
from libc.stdlib cimport malloc, free

# Nakładki
def gcd(unsigned int x, unsigned int y):
    return csample.gcd(x,y)

def in_mandel(x,y,unsigned int n):
    return csample.in_mandel(x,y,n)

def divide(x,y):
    cdef int rem
    quot = csample.divide(x,y,&rem)
    return quot, rem

def avg(double[:] a):
    cdef:
        int sz
        double result

    sz = a.size
    with nogil:
        result = csample.avg(<double *> &a[0], sz)
    return result

# Destruktor do usuwania obiektów typu Point
cdef del_Point(object obj):
    pt = <csample.Point *> PyCapsule_GetPointer(obj,"Point")
    free(<void *> pt)

# Tworzenie obiektu typu Point i zwracanie go jako kapsułki
def Point(double x,double y):
    cdef csample.Point *p
    p = <csample.Point *> malloc(sizeof(csample.Point))
    if p == NULL:
        raise MemoryError("Za mało pamięci na utworzenie obiektu typu Point")
    p.x = x
    p.y = y
    return PyCapsule_New(<void *>p,"Point",<PyCapsule_Destructor>del_Point)

def distance(p1, p2):
    pt1 = <csample.Point *> PyCapsule_GetPointer(p1,"Point")
    pt2 = <csample.Point *> PyCapsule_GetPointer(p2,"Point")
    return csample.distance(pt1,pt2)
