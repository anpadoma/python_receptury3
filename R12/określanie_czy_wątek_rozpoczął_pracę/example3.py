import threading
import time

# Wątek roboczy
def worker(n, sema):
	# Oczekiwanie na sygnał
    sema.acquire()
    # Wykonywanie zadań
    print("Praca", n)

# Tworzenie wątków
sema = threading.Semaphore(0)
nworkers = 10
for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n, sema,))
    t.daemon=True
    t.start()

print('Przed zwolnieniem pierwszego wątku roboczego')
time.sleep(5)
sema.release()
time.sleep(1)
print('Przed zwolnieniem drugiego wątku roboczego')
time.sleep(5)
sema.release()
time.sleep(1)
print('Żegnaj')
