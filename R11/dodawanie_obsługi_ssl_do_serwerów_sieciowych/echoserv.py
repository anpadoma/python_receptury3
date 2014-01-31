from socket import socket, AF_INET, SOCK_STREAM
from socket import SOL_SOCKET, SO_REUSEADDR
import ssl

KEYFILE = 'server_key.pem'   # Klucz prywatny serwera
CERTFILE = 'server_cert.pem' # Certyfikat serwera (przekazywany klientowi)

def echo_client(s):
    while True:
        data = s.recv(8192)
        if data == b'':
            break
        s.send(data)
    s.close()
    print('Połączenie jest zamknięte')

def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(address)
    s.listen(1)
    
	# Dodawanie nakładki z warstwą SSL, wymagającej certyfikatów od klienta
    s_ssl = ssl.wrap_socket(s, 
                            keyfile=KEYFILE, 
                            certfile=CERTFILE, 
                            server_side=True
                            )
    # Oczekiwanie na połączenia
    while True:
        try:
            c,a = s_ssl.accept()
            print('Nawiązano połączenie', c, a)
            echo_client(c)
        except Exception as e:
            print('{}: {}'.format(e.__class__.__name__, e))

echo_server(('', 20000))
