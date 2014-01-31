# Bardzo prosty mechanizm szeregujący dla współprogramów i generatorów

# Dwie proste funkcje generatora
def countdown(n):
    while n > 0:
        print("Odliczanie w dół", n)
        yield
        n -= 1
    print("Start!")

def countup(n):
    x = 0
    while x < n:
        print("Odliczanie w górę", x)
        yield
        x += 1

from collections import deque

class TaskScheduler:
    def __init__(self):
        self._task_queue = deque()

    def new_task(self, task):
        '''
		Przekazywanie uruchomionego właśnie zadania do programu szeregującego
        '''
        self._task_queue.append(task)

    def run(self):
        '''
		Działa dopóty, dopóki istnieją zadania
        '''
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
				# Działa do napotkania następnego polecenia yield
                next(task)
                self._task_queue.append(task)
            except StopIteration:
				# Generator przestał już działać
                pass

# Przykład zastosowania
sched = TaskScheduler()
sched.new_task(countdown(10))
sched.new_task(countdown(5))
sched.new_task(countup(15))
sched.run()
