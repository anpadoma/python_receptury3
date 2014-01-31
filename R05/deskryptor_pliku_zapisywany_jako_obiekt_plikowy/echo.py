from socket import socket, AF_INET, SOCK_STREAM

def echo_client(client_sock, addr):
    print("Żądanie połączenia z", addr)

    # Tworzenie nakładek do odczytu i zapisu danych z gniazd
    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1', closefd=False)
    client_out = open(client_sock.fileno(), 'wt', encoding='latin-1', closefd=False)

    # Wyświetlanie wierszy od klienta za pomocą plikowych operacji wejścia-wyjścia
    for line in client_in:
        client_out.write(line)
        client_out.flush()
    client_sock.close()

def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)

if __name__ == '__main__':
    print('Serwer echo z portu localhost:25000')
    echo_server(('', 25000))
