from socketserver import StreamRequestHandler, TCPServer
import socket

class EchoHandler(StreamRequestHandler):
    timeout = 5
    rbufsize = -1
    wbufsize = 0
    disable_nagle_algorithm = False
    def handle(self):
        print('Żądanie połączenia z', self.client_address)
        # self.rfile to podobny do pliku obiekt używany przy odczycie
        try:
            for line in self.rfile:
                # self.wfile to podobny do pliku obiekt używany przy zapisie
                self.wfile.write(line)
        except socket.timeout:
            print('Przekroczono limit czasu!')

if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    print('Serwer Echo działa w porcie 20000')
    serv.serve_forever()
