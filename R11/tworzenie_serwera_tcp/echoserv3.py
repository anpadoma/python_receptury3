from socketserver import StreamRequestHandler, TCPServer

class EchoHandler(StreamRequestHandler):
    def handle(self):
        print('Żądanie połączenia z', self.client_address)
        # self.rfile to podobny do pliku obiekt używany przy odczycie
        for line in self.rfile:
            # self.wfile to podobny do pliku obiekt używany przy zapisie
            self.wfile.write(line)

if __name__ == '__main__':
    import socket

    serv = TCPServer(('', 20000), EchoHandler, bind_and_activate=False)
    # Ustawianie różnych opcji gniazda
    serv.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # Wiązanie i aktywowanie
    serv.server_bind()
    serv.server_activate()
    print('Serwer Echo działa w porcie 20000')
    serv.serve_forever()
