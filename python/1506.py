"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


# Space O(n)
class Solution:
    def findRoot(self, tree: ['Node']) -> 'Node':
        seen = set()
        for node in tree:
            for child in node.children:
                seen.add(child.val)
        for node in tree:
            if node.val not in seen:
                return node


# Space O(1)
class Solution:
    def findRoot(self, tree: ['Node']) -> 'Node':
        value_sum = 0
        for node in tree:
            value_sum += node.val
            for child in node.children:
                value_sum -= child.val
        for node in tree:
            if node.val == value_sum:
                return node
