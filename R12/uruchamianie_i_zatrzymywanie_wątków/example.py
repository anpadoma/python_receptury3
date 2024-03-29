from threading import Thread
import time

class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print("Odliczanie w dół", n)
            n -= 1
            time.sleep(5)

c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()

time.sleep(20)
print('Przed zakończeniem')
c.terminate()
t.join()
print('Zakończono')

