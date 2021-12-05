from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/house-robber-iii/discuss/79394/Python-O(n)-code%3A-Optimized-for-Readability
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.helper(root))

    def helper(self, node):
        if not node:
            return 0, 0

        left, right = self.helper(node.left), self.helper(node.right)

        now = node.val + left[1] + right[1]
        later = max(left) + max(right)

        return now, later
