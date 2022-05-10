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

    def get_data_node(self, key):
        index = self.hash(key)
        return self.data[index]

    def put(self, key: int, value: int) -> None:
        curr = self.get_data_node(key)
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = Node(key, value)

    def get(self, key: int) -> int:
        curr = self.get_data_node(key)
        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        curr = self.get_data_node(key)
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
