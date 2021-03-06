from typing import List
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/discuss/231256/python-queue-%2B-hash-map
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        g = defaultdict(list)
        queue = [(root, 0)]
        while queue:
            new = []
            d = defaultdict(list)
            for node, order in queue:
                d[order].append(node.val)
                if node.left:
                    new.append((node.left, order - 1))
                if node.right:
                    new.append((node.right, order + 1))
            for order in d:
                g[order].extend(sorted(d[order]))
            queue = new
        return [g[order] for order in sorted(g)]
