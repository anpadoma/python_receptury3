from collections import deque

class ActorScheduler:
    def __init__(self):
        self._actors = { }          # Odwzorowywanie nazw na aktory
        self._msg_queue = deque()   # Kolejka komunikatów
    
    def new_actor(self, name, actor):
        '''
		Przekazywanie uruchomionego aktora do mechanizmu szeregującego i nadawanie aktorowi nazwy
        '''
        self._msg_queue.append((actor,None))
        self._actors[name] = actor

    def send(self, name, msg):
        '''
		Wysyłanie komunikatu do aktora o określonej nazwie
        '''
        actor = self._actors.get(name)
        if actor:
            self._msg_queue.append((actor,msg))

    def run(self):
        '''
		Działa dopóty, dopóki istnieją oczekujące komunikaty
        '''
        while self._msg_queue:
            actor, msg = self._msg_queue.popleft()
            try:
                 actor.send(msg)
            except StopIteration:
                 pass

# Przykład zastosowania
if __name__ == '__main__':
    def printer():
        while True:
            msg = yield
            print('Otrzymano:', msg)

    def counter(sched):
        while True:
			# Pobieranie aktualnej wartości licznika
            n = yield    
            if n == 0:
                break
			# Wysyłanie danych do zadania printer
            sched.send('printer', n)
            # Wysyłanie następnej wartości do zadania counter (rekurencyjnie)
            sched.send('counter', n-1)

    sched = ActorScheduler()
    # Tworzenie początkowych aktorów
    sched.new_actor('printer', printer())
    sched.new_actor('counter', counter(sched))

	# Wysyłanie początkowego komunikatu do zadania counter w celu rozpoczęcia pracy
    sched.send('counter', 10000)
    sched.run()
