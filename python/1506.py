# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


# Space O(1)
class Solution:
    def findRoot(self, tree: ['Node']) -> 'Node':
        sum = 0
        for node in tree:
            sum += node.val
            for c in node.next:
                sum -= c.val
        for node in tree:
            if sum == node.val:
                return node


# Space O(n)
class Solution:
    def findRoot(self, tree: ['Node']) -> 'Node':
        seen = set()
        for node in tree:
            for c in node.next:
                seen.add(c)
        for node in tree:
            if node not in seen:
                return node
