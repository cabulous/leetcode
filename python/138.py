# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# Recursive
class Solution:

    def __init__(self):
        self.memo = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        if head in self.memo:
            return self.memo[head]

        clone = Node(head.val)
        self.memo[head] = clone

        clone.next = self.copyRandomList(head.next)
        clone.random = self.copyRandomList(head.random)

        return clone


# Iterative
class Solution:
    def __init__(self):
        self.visited = {}

    def get_cloned_node(self, node):
        if not node:
            return None
        if node in self.visited:
            return self.visited[node]
        self.visited[node] = Node(node.val)
        return self.visited[node]

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        old_node = head
        new_node = Node(head.val)
        self.visited[old_node] = new_node
        while old_node:
            new_node.next = self.get_cloned_node(old_node.next)
            new_node.random = self.get_cloned_node(old_node.random)
            old_node = old_node.next
            new_node = new_node.next
        return self.visited[head]
