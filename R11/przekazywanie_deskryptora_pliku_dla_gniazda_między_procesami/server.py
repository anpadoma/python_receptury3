# server.py
import socket
import struct

def send_fd(sock, fd):
    '''
    Wysyłanie jednego deskryptora pliku.
    '''
    sock.sendmsg([b'x'],
                 [(socket.SOL_SOCKET, socket.SCM_RIGHTS, struct.pack('i', fd))])
    ack = sock.recv(2)
    assert ack == b'OK'

def server(work_address, port):
    # Oczekiwanie na połączenie wątku roboczego
    work_serv = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    work_serv.bind(work_address)
    work_serv.listen(1)
    worker, addr = work_serv.accept()

    # Uruchamianie serwera TCP/IP i wysyłanie klientów dowątku roboczego
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    s.bind(('',port))
    s.listen(1)
    while True:
        client, addr = s.accept()
        print('SERWER: Żądanie połączenia z', addr)
        send_fd(worker, client.fileno())
        client.close()
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('Stosowanie: server.py server_address port', file=sys.stderr)
        raise SystemExit(1)

    server(sys.argv[1], int(sys.argv[2]))
