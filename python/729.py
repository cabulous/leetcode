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

    def _insert_node(self, node: Node, curr_node: Node) -> bool:
        if curr_node.end <= node.start:
            if curr_node.right is None:
                curr_node.right = node
                return True
            return self._insert_node(node, curr_node.right)

        if node.end <= curr_node.start:
            if curr_node.left is None:
                curr_node.left = node
                return True
            return self._insert_node(node, curr_node.left)

        return False


class MyCalendar:

    def __init__(self):
        self.root = Tree()

    def book(self, start: int, end: int) -> bool:
        return self.root.insert(Node(start, end))
