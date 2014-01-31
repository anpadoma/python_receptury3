from socketserver import StreamRequestHandler, TCPServer

class EchoHandler(StreamRequestHandler):
    def handle(self):
        print('Żądanie połączenia z', self.client_address)
        # self.rfile to podobny do pliku obiekt używany przy odczycie
        for line in self.rfile:
            # self.wfile to podobny do pliku obiekt używany przy zapisie
            self.wfile.write(line)

if __name__ == '__main__':
    from threading import Thread
    NWORKERS = 16
    serv = TCPServer(('', 20000), EchoHandler)
    for n in range(NWORKERS):
        t = Thread(target=serv.serve_forever)
        t.daemon = True
        t.start()
    print('Serwer wielowątkowy działa w porcie 20000')
    serv.serve_forever()
