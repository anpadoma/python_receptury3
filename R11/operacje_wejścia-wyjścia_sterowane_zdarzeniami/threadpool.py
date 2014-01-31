import socket
from concurrent.futures import ThreadPoolExecutor
from eventhandler import EventHandler, event_loop

class ThreadPoolHandler(EventHandler):
    def __init__(self, nworkers):
        self.signal_done_sock, self.done_sock = socket.socketpair()
        self.pending = []
        self.pool = ThreadPoolExecutor(nworkers)
        
    def fileno(self):
        return self.done_sock.fileno()

	# Wywołanie zwrotne uruchamiane po zakończeniu pracy przez wątek
    def _complete(self, callback, r):
        self.pending.append((callback, r.result()))
        self.signal_done_sock.send(b'x')

    # Uruchamianie funkcji z puli wątków
    def run(self, func, args=(), kwargs={},*,callback):
        r = self.pool.submit(func, *args, **kwargs)
        r.add_done_callback(lambda r: self._complete(callback, r))

    def wants_to_receive(self):
        return True

	# Uruchamia wywołania zwrotne po zakończeniu pracy
    def handle_receive(self):
		# Uruchamianie wszystkich oczekujących wywołań zwrotnych
        for callback, result in self.pending:
            callback(result)
            self.done_sock.recv(1)
        self.pending = []

# Bardzo kiepska implementacja wyznaczania liczb Fibonacciego
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

class UDPServer(EventHandler):
    def __init__(self, address):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(address)

    def fileno(self):
        return self.sock.fileno()

    def wants_to_receive(self):
        return True
    
class UDPFibServer(UDPServer):
    def handle_receive(self):
        msg, addr = self.sock.recvfrom(128)
        n = int(msg)
        pool.run(fib, (n,), callback=lambda r: self.respond(r, addr))

    def respond(self, result, addr):
        self.sock.sendto(str(result).encode('ascii'), addr)

if __name__ == '__main__':
    pool = ThreadPoolHandler(16)
    handlers = [ pool, UDPFibServer(('',16000))]
    event_loop(handlers)
