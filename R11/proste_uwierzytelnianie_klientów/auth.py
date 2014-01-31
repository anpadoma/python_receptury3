# auth.py

import hmac
import os

def client_authenticate(connection, secret_key):
    '''
	Uwierzytelnianie klienta w zdalnej usłudze.
	connection to połączenie sieciowe, a secret_key to
	klucz znany tylko klientowi i serwerowi.
    '''
    message = connection.recv(32)
    hash = hmac.new(secret_key, message)
    digest = hash.digest()
    connection.send(digest)

def server_authenticate(connection, secret_key):
    '''
    Żądanie uwierzytelnienia klienta.
    '''
    message = os.urandom(32)
    connection.send(message)
    hash = hmac.new(secret_key, message)
    digest = hash.digest()
    response = connection.recv(len(digest))
    return hmac.compare_digest(digest,response)
