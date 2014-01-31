# echoclient.py
#
# Przykładowy klient łączący się z serwerem SSL i 
# sprawdzający jego certyfikat

from socket import socket, AF_INET, SOCK_STREAM
import ssl

s = socket(AF_INET, SOCK_STREAM)

# Dodawanie nakładki z warstwą SSL i wymaganie od serwera przedstawienia
# certyfikatu
ssl_s = ssl.wrap_socket(s,
                        cert_reqs=ssl.CERT_REQUIRED,
                        ca_certs='server_cert.pem',
                        )

ssl_s.connect(('localhost', 20000))

# Komunikowanie się z serwerem
ssl_s.send(b'Witaj, Polsko!')
resp = ssl_s.recv(8192)
print('Otrzymano:', resp)

# Gotowe
ssl_s.close()
