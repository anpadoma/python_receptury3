import threading
import time

class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        '''
		Uruchamianie zegara i powiadamianie wątków oczekujących po każdym przedziale czasu
        '''
        while True:
            time.sleep(self._interval)
            with self._cv:
                 self._flag ^= 1
                 self._cv.notify_all()

    def wait_for_tick(self):
        '''
		Oczekiwanie na następny takt zegara
        '''
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()

# Przykład zastosowania zegara
ptimer = PeriodicTimer(5)
ptimer.start()

# Dwa wątki synchronizująca pracę na podstawie zegara
def countdown(nticks):
    while nticks > 0:
        ptimer.wait_for_tick()
        print("Odliczanie w dół", nticks)
        nticks -= 1

def countup(last):
    n = 0
    while n < last:
        ptimer.wait_for_tick()
        print("Odliczanie", n)
        n += 1

threading.Thread(target=countdown, args=(10,)).start()
threading.Thread(target=countup, args=(5,)).start()
