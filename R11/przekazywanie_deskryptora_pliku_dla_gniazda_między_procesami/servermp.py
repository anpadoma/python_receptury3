# servermp.py
from multiprocessing.connection import Listener
from multiprocessing.reduction import send_handle
import socket

def server(work_address, port):
    # Oczekiwanie na połączenie z wątkiem roboczym
    work_serv = Listener(work_address, authkey=b'peekaboo')
    worker = work_serv.accept()
    worker_pid = worker.recv()

	# Uruchamianie serwera TCP/IP i wysyłanie klientó do wątku roboczego
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    s.bind(('', port))
    s.listen(1)
    while True:
        client, addr = s.accept()
        print('SERWER: Żądanie połączenia z', addr)
        send_handle(worker, client.fileno(), worker_pid)
        client.close()
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('Stosowanie: server.py server_address port', file=sys.stderr)
        raise SystemExit(1)

    server(sys.argv[1], int(sys.argv[2]))
