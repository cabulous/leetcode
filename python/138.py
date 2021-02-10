# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# Recursive
class Solution:
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        if head in self.visited:
            return self.visited[head]
        node = Node(head.val, None, None)
        self.visited[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node


# Iterative
class Solution:
    def __init__(self):
        self.visited = {}

    def get_cloned_node(self, node):
        if node:
            if node in self.visited:
                return self.visited[node]
            self.visited[node] = Node(node.val, None, None)
            return self.visited[node]
        return None

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        old_node = head
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node
        while old_node:
            new_node.random = self.get_cloned_node(old_node.random)
            new_node.next = self.get_cloned_node(old_node.next)
            old_node = old_node.next
            new_node = new_node.next
        return self.visited[head]
