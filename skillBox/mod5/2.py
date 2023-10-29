class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = None
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            removed = self.head
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
            return removed.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

# Пример использования:

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(f"Первый элемент в очереди: {queue.peek()}")  # Выведет: 1

dequeued_element = queue.dequeue()
print(f"Извлеченный элемент: {dequeued_element}")  # Выведет: 1

print(f"Первый элемент в очереди после извлечения: {queue.peek()}")  # Выведет: 2
