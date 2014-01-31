from actor import Actor

class TaggedActor(Actor):
    def run(self):
        while True:
             tag, *payload = self.recv()
             getattr(self,"do_"+tag)(*payload)
    
	# Metody odpowiadające różnym etykietom z komunikatów
    def do_A(self, x):
        print("Uruchamia A", x)

    def do_B(self, x, y):
        print("Uruchamia B", x, y)

# Przykład
if __name__ == '__main__':
    a = TaggedActor()
    a.start()
    a.send(('A', 1))      # Wywołuje do_A(1)
    a.send(('B', 2, 3))   # Wywołuje do_B(2,3)
    a.close()
    a.join()

