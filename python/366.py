from collections import defaultdict
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/find-leaves-of-binary-tree/discuss/83815/Simple-Python-solution-using-dict
class Solution:

    def __init__(self):
        self.nodes = defaultdict(list)

    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        self.collect_leaves(root)

        res = []
        for height in range(1, len(self.nodes) + 1):
            res.append(self.nodes[height])

        return res

    def collect_leaves(self, node):
        if node is None:
            return 0

        left_height = self.collect_leaves(node.left)
        right_height = self.collect_leaves(node.right)

        height = max(left_height, right_height) + 1
        self.nodes[height].append(node.val)

        return height
