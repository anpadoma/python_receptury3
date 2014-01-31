import ctypes
lib = ctypes.cdll.LoadLibrary(None)

# Pobieranie adresu funkcji sin() z biblioteki math języka C
addr = ctypes.cast(lib.sin, ctypes.c_void_p).value
print(addr)
140735505915760

# Przekształcanie adresu w jednostkę wywoływalną
functype = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
func = functype(addr)
print(func)

# Wywołanie uzyskanej funkcji
print(func(2))
print(func(0))
