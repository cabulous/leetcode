from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# Recursive
class Solution:

    def __init__(self):
        self.memo = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
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
        self.memo = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_node = head
        new_node = self.get_clone(head)

        while old_node:
            new_node.next = self.get_clone(old_node.next)
            new_node.random = self.get_clone(old_node.random)
            old_node = old_node.next
            new_node = new_node.next

        return self.get_clone(head)

    def get_clone(self, node):
        if node is None:
            return None
        if node in self.memo:
            return self.memo[node]
        clone = Node(node.val)
        self.memo[node] = clone
        return self.memo[node]
