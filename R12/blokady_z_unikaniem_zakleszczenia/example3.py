import threading
from deadlock import acquire

# Wątek filozofa
def philosopher(left, right):
    while True:
        with acquire(left,right):
             print(threading.currentThread(), 'jedzenie')

# Pałeczki (reprezentowane za pomocą blokad)
NSTICKS = 5
chopsticks = [threading.Lock() for n in range(NSTICKS)]

# Tworzenie wszystkich filozofów
for n in range(NSTICKS):
    t = threading.Thread(target=philosopher,
                         args=(chopsticks[n],chopsticks[(n+1) % NSTICKS]))
    t.daemon = True
    t.start()

import time
while True:
    time.sleep(1)



