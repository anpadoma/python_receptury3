cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef clip(double[:] a, double min, double max, double[:] out):
    '''
    Przycinanie wartości do przedziału min - max. Wynika zapisywany w argumencie out
    '''
    if min > max:
        raise ValueError("min musi być <= max")
    if a.shape[0] != out.shape[0]:
        raise ValueError("Tablice wejściowa i wyjściowa muszą mieć tę samą wielkość")
    for i in range(a.shape[0]):
        if a[i] < min:
            out[i] = min
        elif a[i] > max:
            out[i] = max
        else:
            out[i] = a[i]

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef clip_fast(double[:] a, double min, double max, double[:] out):
    if min > max:
        raise ValueError("min musi być <= max")
    if a.shape[0] != out.shape[0]:
        raise ValueError("Tablice wejściowa i wyjściowa muszą mieć tę samą wielkość")
    for i in range(a.shape[0]):
        out[i] = (a[i] if a[i] < max else max) if a[i] > min else min

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef clip2d(double[:,:] a, double min, double max, double[:,:] out):
    if min > max:
        raise ValueError("min musi być <= max")
    for n in range(a.ndim):
        if a.shape[n] != out.shape[n]:
            raise TypeError("a i out mają inną budowę")
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            if a[i,j] < min:
                out[i,j] = min
            elif a[i,j] > max:
                out[i,j] = max
            else:
                out[i,j] = a[i,j]
