# Skomplikowany przykład iterowania wgłąb za pomocą iteratora

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node(%r)' % self._value

    def add_child(self, other_node):
        self._children.append(other_node)
 
    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)

class DepthFirstIterator(object):
    '''
    Przechodzenie wgłąb
    '''
    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        # Zwracanie bieżącego obiektu, jeśli jest to pierwsze wywołanie,
		# i tworzenie iteratorów dla obiektów podrzędnych
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node

        # Jeśli przetwarzany jest obiekt podrzędny, należy zwrócić 
		# jego następny element
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)

        # Przechodzenie do następnego obiektu podrzędnego i
		# rozpoczęcie iterowania po nim
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)


# Przykład
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)
    # Zwraca: Node(0), Node(1), Node(3), Node(4), Node(2), Node(5)
