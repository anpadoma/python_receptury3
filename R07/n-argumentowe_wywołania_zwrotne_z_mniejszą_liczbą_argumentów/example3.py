# Używanie funkcji partial do przekazywania dodatkowych argumentów do konstruktora klasy
from socketserver import StreamRequestHandler, TCPServer

class EchoHandler(StreamRequestHandler):
    # ack to dodawany argument przekazywany tylko za pomocą słowa kluczowego. *args, **kwargs to
    # standardowe argumenty (przekazywane dalej)
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)
    def handle(self):
        for line in self.rfile:
            self.wfile.write(self.ack + line)

if __name__ == '__main__':
    from functools import partial
    serv = TCPServer(('', 15000), partial(EchoHandler, ack=b'RECEIVED:'))
    print('Serwer Echo działa w porcie 15000')
    serv.serve_forever()
