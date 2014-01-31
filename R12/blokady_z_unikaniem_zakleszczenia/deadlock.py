import threading
from contextlib import contextmanager

# Lokalny stan wątku na informacje dotyczące zajętych już blokad
_local = threading.local()

@contextmanager
def acquire(*locks):
	# Sortowanie blokad na podstawie identyfikatorów obiektów
    locks = sorted(locks, key=lambda x: id(x))   

	# Upewnianie się, że kolejność wcześniej zajętych blokad nie jest naruszona
    acquired = getattr(_local, 'acquired',[])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Naruszenie kolejności blokad')

	# Zajmowanie wszystkich blokad
    acquired.extend(locks)
    _local.acquired = acquired
    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
	    # Zwalnianie blokad w kolejności odwrotnej do ich zajmowania
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]
