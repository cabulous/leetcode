class Node:

    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:

    def __init__(self):
        self.key_range = 1000
        self.data = [Node() for _ in range(self.key_range)]

    def hash(self, key):
        return key % self.key_range

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        head = self.data[index]
        while head.next:
            if head.next.key == key:
                head.next.val = value
                return
            head = head.next
        head.next = Node(key, value)

    def get(self, key: int) -> int:
        index = self.hash(key)
        head = self.data[index]
        while head.next:
            if head.next.key == key:
                return head.next.val
            head = head.next
        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        head = self.data[index]
        while head.next:
            if head.next.key == key:
                head.next = head.next.next
                return
            head = head.next
