class Node:

    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class DoubleLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node: Node):
        self.tail.prev.next, self.tail.prev, node.next, node.prev = node, node, self.tail, self.tail.prev

    def remove(self, node: Node):
        node.prev.next, node.next.prev = node.next, node.prev
        node.next = None
        node.prev = None

    def move_to_tail(self, node: Node):
        self.remove(node)
        self.add(node)

    def remove_head(self) -> Node:
        node = self.head.next
        self.remove(node)
        return node


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.ordered_cache = DoubleLinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.ordered_cache.move_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.ordered_cache.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.ordered_cache.add(node)
        if len(self.cache) > self.capacity:
            node = self.ordered_cache.remove_head()
            del self.cache[node.key]
