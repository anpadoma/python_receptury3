class EventHandler:
    def fileno(self):
		'Zwraca powiązany deskryptor pliku'
        raise NotImplemented('Do napisania')

    def wants_to_receive(self):
        'Zwraca True, jeśli przyjmuje dane'
        return False

    def handle_receive(self):
        'Obsługuje przyjmowanie danych'
        pass

    def wants_to_send(self):
        'Zwraca True, jeśli wysyła dane' 
        return False

    def handle_send(self):
        'Wysyła wychodzące dane'
        pass

import select

def event_loop(handlers):
    while True:
        wants_recv = [h for h in handlers if h.wants_to_receive()]
        wants_send = [h for h in handlers if h.wants_to_send()]
        can_recv, can_send, _ = select.select(wants_recv, wants_send, [])
        for h in can_recv:
            h.handle_receive()
        for h in can_send:
            h.handle_send()
