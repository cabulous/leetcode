from threading import Lock


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


# Singly-Linked List
class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.count = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.count == self.capacity:
            return False
        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.head = self.head.next
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.head.value

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.tail.value

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


# array + Thread-Safe
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.capacity = k
        self.count = 0
        self.head_index = 0
        self.queue_lock = Lock()

    def enQueue(self, value: int) -> bool:
        with self.queue_lock:
            if self.count == self.capacity:
                return False
            self.queue[(self.head_index + self.count) % self.capacity] = value
            self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.head_index = (self.head_index + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.head_index]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[(self.head_index + self.count - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity
