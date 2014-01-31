from collections import deque
from select import select

# Ta klasa reprezentuje uniwersalne zdarzenie generowania w mechanizmie szeregującym
class YieldEvent:
    def handle_yield(self, sched, task):
        pass
    def handle_resume(self, sched, task):
        pass

# Mechanizm szeregujący zadania
class Scheduler:
    def __init__(self):
        self._numtasks = 0       # Łączna liczba zadań
        self._ready = deque()    # Zadania gotowe do uruchomienia
        self._read_waiting = {}  # Zadania oczekujące na odczyt
        self._write_waiting = {} # Zadania oczekujące na zapis
    
	# Sprawdzanie zdarzeń wejścia-wyjścia i ponowne uruchamianie oczekujących zadań
    def _iopoll(self):
        rset,wset,eset = select(self._read_waiting,
                                self._write_waiting,[])
        for r in rset:
            evt, task = self._read_waiting.pop(r)
            evt.handle_resume(self, task)
        for w in wset:
            evt, task = self._write_waiting.pop(w)
            evt.handle_resume(self, task)

    def new(self,task):
        '''
		Dodawanie uruchomionego zadania do mechanizmu szeregującego
        '''
        self._ready.append((task, None))
        self._numtasks += 1

    def add_ready(self, task, msg=None):
        '''
		Umieszczanie uruchomionego już zadania do kolejki gotowych zadań.
		msg to komunikat przekazywany do zadania przy wznawianiu pracy
        '''
        self._ready.append((task, msg))

	# Dodawanie zadania do zbioru zadań oczekujących na odczyt
    def _read_wait(self, fileno, evt, task):
        self._read_waiting[fileno] = (evt, task)

	# Dodawanie zadania do zbioru zadań oczekujących na zapis
    def _write_wait(self, fileno, evt, task):
        self._write_waiting[fileno] = (evt, task)

    def run(self):
        '''
		Uruchamia mechanizm szeregujący zadania dopóty, dopóki istnieją zadania
        '''
        while self._numtasks:
             if not self._ready:
                  self._iopoll()
             task, msg = self._ready.popleft()
             try:
				 # Uruchamia współprogram do następnego wywołania yield
                 r = task.send(msg)
                 if isinstance(r, YieldEvent):
                     r.handle_yield(self, task)
                 else:
                     raise RuntimeError('Nierozpoznane zdarzenie generowania')
             except StopIteration:
                 self._numtasks -= 1

# Przykładowa implementacja operacji wejścia-wyjścia gniazd oparta na współprogramach
class ReadSocket(YieldEvent): 
    def __init__(self, sock, nbytes):
        self.sock = sock
        self.nbytes = nbytes
    def handle_yield(self, sched, task):
        sched._read_wait(self.sock.fileno(), self, task)
    def handle_resume(self, sched, task):
        data = self.sock.recv(self.nbytes)
        sched.add_ready(task, data)

class WriteSocket(YieldEvent): 
    def __init__(self, sock, data):
        self.sock = sock
        self.data = data
    def handle_yield(self, sched, task):
        sched._write_wait(self.sock.fileno(), self, task)
    def handle_resume(self, sched, task):
        nsent = self.sock.send(self.data)
        sched.add_ready(task, nsent)

class AcceptSocket(YieldEvent): 
    def __init__(self, sock):
        self.sock = sock
    def handle_yield(self, sched, task):
        sched._read_wait(self.sock.fileno(), self, task)
    def handle_resume(self, sched, task):
        r = self.sock.accept()
        sched.add_ready(task, r)

# Nakładka na obiekt gniazda używana dla operacji yield
class Socket(object):
    def __init__(self, sock):
        self._sock = sock
    def recv(self, maxbytes):
        return ReadSocket(self._sock, maxbytes)
    def send(self, data):
        return WriteSocket(self._sock, data)
    def accept(self):
        return AcceptSocket(self._sock)
    def __getattr__(self, name):
        return getattr(self._sock, name)

if __name__ == '__main__':
    from socket import socket, AF_INET, SOCK_STREAM
    import time

	# Przykładowa funkcja z generatorami. Należy ją wywoływać w następujący sposób:
	# line = yield from readline(sock)
    def readline(sock):
        chars = []
        while True:
            c = yield sock.recv(1)
            if not c:
                break
            chars.append(c)
            if c == b'\n':
                break
        return b''.join(chars)
		
	# Serwer Echo używający generatorów
    class EchoServer:
        def __init__(self,addr,sched):
            self.sched = sched
            sched.new(self.server_loop(addr))

        def server_loop(self,addr):
            s = Socket(socket(AF_INET,SOCK_STREAM))
            s.bind(addr)
            s.listen(5)
            while True:
                c,a = yield s.accept()
                print('Żądanie połączenia z ', a)
                self.sched.new(self.client_handler(Socket(c)))

        def client_handler(self,client):
            while True:
                line = yield from readline(client)
                if not line:
                    break
                line = b'OTRZYMANO:' + line
                while line:
                    nsent = yield client.send(line)
                    line = line[nsent:]
            client.close()
            print('Klient został zamknięty')

    sched = Scheduler()
    EchoServer(('',16000),sched)
    sched.run()
