from typing import Optional


class Node:

    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class Tree:

    def __init__(self):
        self.root = Node()

    def insert(self, node: Node) -> bool:
        return self._insert_node(node, self.root)

    def _insert_node(self, node: Node, curr: Node) -> bool:
        if node.start >= curr.end:
            if curr.right is None:
                curr.right = node
                return True
            return self._insert_node(node, curr.right)

        if node.end <= curr.start:
            if curr.left is None:
                curr.left = node
                return True
            return self._insert_node(node, curr.left)

        return False


class MyCalendar:

    def __init__(self):
        self.root = Tree()

    def book(self, start: int, end: int) -> bool:
        node = Node(start, end)
        return self.root.insert(node)
