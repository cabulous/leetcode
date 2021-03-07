class MyHashMap:

    def __init__(self):
        self.data = [Node() for _ in range(1000)]

    def hashcode(self, key):
        size = len(self.data)
        return key % size

    def put(self, key: int, value: int) -> None:
        hashcode = self.hashcode(key)
        head = self.data[hashcode]
        while head.next:
            if head.next.key == key:
                head.next.value = value
                return
            head = head.next
        head.next = Node(key, value)

    def get(self, key: int) -> int:
        hashcode = self.hashcode(key)
        head = self.data[hashcode]
        while head.next:
            if head.next.key == key:
                return head.next.value
            head = head.next
        return -1

    def remove(self, key: int) -> None:
        hashcode = self.hashcode(key)
        head = self.data[hashcode]
        while head.next:
            if head.next.key == key:
                to_remove = head.next
                head.next, to_remove.next = to_remove.next, None
                return
            head = head.next


class Node:
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.value = value
        self.next = next
