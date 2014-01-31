from threading import Thread, Event
import time

# Kod do wykonywania w niezależnym wątku
def countdown(n, started_evt):
    print("Rozpoczynanie odliczania")
    started_evt.set() 
    while n > 0:
        print("Odliczanie w dół", n)
        n -= 1
        time.sleep(5)

# Tworzenie obiektu zdarzenia używanego do sygnalizowania rozpoczęcia pracy
started_evt = Event()

# Uruchamianie wątku i przekazywanie zdarzenia startowego
print("Uruchamianie odliczania")
t = Thread(target=countdown, args=(10,started_evt))
t.start()

# Oczekiwanie na rozpoczęcie pracy przez wątek
started_evt.wait()
print("Odliczanie w toku")
