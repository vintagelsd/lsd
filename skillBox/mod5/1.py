class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped = self.top
            self.top = self.top.next
            return popped.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.top.data

#Пример
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(f"Текущий верхний элемент: {stack.peek()}")

popped_element = stack.pop()

print(f"Извлеченный элемент: {popped_element}")

print(f"Текущий верхний элемент: {stack.peek()}")
