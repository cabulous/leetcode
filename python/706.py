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
        curr = self.data[index]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = Node(key, value)

    def get(self, key: int) -> int:
        index = self.hash(key)
        curr = self.data[index]
        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        curr = self.data[index]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
