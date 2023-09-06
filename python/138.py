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

        return self.memo[head]


# Iterative
class Solution:

    def __init__(self):
        self.memo = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        clone = self.get_clone(head)

        while curr:
            clone.next = self.get_clone(curr.next)
            clone.random = self.get_clone(curr.random)
            curr = curr.next
            clone = clone.next

        return self.get_clone(head)

    def get_clone(self, node):
        if node is None:
            return None
        if node in self.memo:
            return self.memo[node]
        self.memo[node] = Node(node.val)
        return self.memo[node]
