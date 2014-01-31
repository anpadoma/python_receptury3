import threading
from deadlock import acquire

x_lock = threading.Lock()
y_lock = threading.Lock()

def thread_1():
    while True:
        with acquire(x_lock, y_lock):
            print("Wątek-1")

def thread_2():
    while True:
        with acquire(y_lock, x_lock):
            print("Wątek-2")

input('Ten program działa w nieskończoność. Wciśnij [Enter], aby rozpocząć, i Ctrl-C, aby zakończyć')

t1 = threading.Thread(target=thread_1)
t1.daemon = True
t1.start()

t2 = threading.Thread(target=thread_2)
t2.daemon = True
t2.start()

import time
while True:
    time.sleep(1)
