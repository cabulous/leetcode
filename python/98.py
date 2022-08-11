import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, -math.inf, math.inf)

    def helper(self, node, lo, hi):
        if node is None:
            return True

        if node.val <= lo or hi <= node.val:
            return False

        return self.helper(node.left, lo, node.val) and self.helper(node.right, node.val, hi)
