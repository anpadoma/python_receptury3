# rpcserver.py

import pickle
class RPCHandler:
    def __init__(self):
        self._functions = { }

    def register_function(self, func):
        self._functions[func.__name__] = func

    def handle_connection(self, connection):
        try:
            while True:
                # Otrzymywanie komunikatu
                func_name, args, kwargs = pickle.loads(connection.recv())
                # Uruchamianie wywołania RPC i wysyłanie odpowiedzi
                try:
                    r = self._functions[func_name](*args,**kwargs)
                    connection.send(pickle.dumps(r))
                except Exception as e:
                    connection.send(pickle.dumps(e))
        except EOFError:
             pass

# Przykład zastosowania
from multiprocessing.connection import Listener
from threading import Thread

def rpc_server(handler, address, authkey):
    sock = Listener(address, authkey=authkey)
    while True:
        client = sock.accept()
        t = Thread(target=handler.handle_connection, args=(client,))
        t.daemon = True
        t.start()

# Zdalnie wywoływane funkcje
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

# Rejestrowanie funkcji w obiekcie handler
handler = RPCHandler()
handler.register_function(add)
handler.register_function(sub)

# Uruchamianie serwera
rpc_server(handler, ('localhost', 17000), authkey=b'peekaboo')
