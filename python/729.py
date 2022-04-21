class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.binary_insert(node)
        if node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.binary_insert(node)
        return False


class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        node = Node(start, end)
        if not self.root:
            self.root = node
            return True
        return self.root.binary_insert(node)
