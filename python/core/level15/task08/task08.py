# Очередь это сложно

# Напишите программу, которая реализует очередь и демонстрирует ее основные свойства:
# FIFO (First In, First Out), операции enqueue, dequeue, и peek.

# Класс list использовать нельзя.
from collections import

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
    # инициализация очереди

    def enqueue(self, value):
    # добавление элемента

    def dequeue(self):
    # удаление и возвращение элемента

    def peek(self):
    # возвращение первого элемента без удаления

    def is_empty(self):
        return self.front is None

    def display(self):
        current = self.front
        values = []
        while current is not None:
            values.append(current.value)
            current = current.next
        return values

# Демонстрация функционирования
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue after enqueues:", queue.display())
print("Peek:", queue.peek())
print("Dequeue:", queue.dequeue())
print("Queue after dequeue:", queue.display())
print("Dequeue:", queue.dequeue())
print("Queue after dequeue:", queue.display())
print("Dequeue:", queue.dequeue())
print("Queue after dequeue:", queue.display())