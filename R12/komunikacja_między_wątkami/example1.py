from queue import Queue
from threading import Thread
import time

_sentinel = object()

# Wątek generujący dane
def producer(out_q):
    n = 10
    while n > 0:
        # Generowanie danych
        out_q.put(n)
        time.sleep(2)
        n -= 1

    # Umieszczanie w kolejce wartownika informującego o zakończeniu pracy
    out_q.put(_sentinel)

# Wątek używający danych
def consumer(in_q):
    while True:
        # Pobieranie danych
        data = in_q.get()

        # Sprawdzanie, czy nie zakończono pracy
        if data is _sentinel:
            in_q.put(_sentinel)
            break

        # Przetwarzanie danych
        print('Otrzymano:', data)
    print('Konsument kończy pracę')

if __name__ == '__main__':
    q = Queue()
    t1 = Thread(target=consumer, args=(q,))
    t2 = Thread(target=producer, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

