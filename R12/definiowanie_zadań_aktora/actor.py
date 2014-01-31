from queue import Queue
from threading import Thread, Event

# Wartownik używany do kończenia pracy
class ActorExit(Exception):
    pass

class Actor:
    def __init__(self):
        self._mailbox = Queue()

    def send(self, msg):
        '''
		Wysyłanie komunikatu do aktora
        '''
        self._mailbox.put(msg)

    def recv(self):
        '''
        Odbieranie przychodzących komunikatów
        '''
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def close(self):
        '''
		Zamykanie aktora i kończenie pracy
        '''
        self.send(ActorExit)

    def start(self):
        '''
		Rozpoczynanie równoległego wykonywania
        '''
        self._terminated = Event()
        t = Thread(target=self._bootstrap)
        t.daemon = True
        t.start()

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()

    def join(self):
        self._terminated.wait()

    def run(self):
        '''
		Uruchamianie metody, którą powinien napisać użytkownik
        '''
        while True:
            msg = self.recv()

# Przykładowe zadanie
class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print("Odebrane:", msg)

if __name__ == '__main__':
    # Przykład zastosowania
    p = PrintActor()
    p.start()
    p.send("Witaj")
    p.send("Polsko")
    p.close()
    p.join()

