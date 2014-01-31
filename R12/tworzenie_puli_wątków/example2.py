from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from queue import Queue

def echo_client(q):
    '''
	Obsługa połączenia z klientem
    '''
    sock, client_addr = q.get()
    print('Żądanie połączenia z', client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print('Klient zamknął połączenie')
    sock.close()

def echo_server(addr, nworkers):
    print('Serwer Echo działa pod adresem', addr)
	# Uruchamianie wątków roboczych dla klienta
    q = Queue()
    for n in range(nworkers):
        t = Thread(target=echo_client, args=(q,))
        t.daemon = True
        t.start()

    # Uruchamianie serwera
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        q.put((client_sock, client_addr))

echo_server(('',15000), 128)
