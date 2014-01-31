# example.py
#
# Tworzenie kolejki priorytetowej

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

# Przykład wykorzystania kolejki
class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

print("Oczekiwana wartość to bar:", q.pop())
print("Oczekiwana wartość to spam:", q.pop())
print("Oczekiwana wartość to foo:", q.pop())
print("Oczekiwana wartość to grok:", q.pop())
