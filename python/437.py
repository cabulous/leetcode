from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.target_sum = 0
        self.count = 0
        self.all_sums = defaultdict(int)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.target_sum = targetSum
        self.preorder(root, 0)
        return self.count

    def preorder(self, node, cur_sum):
        if not node:
            return

        cur_sum += node.val

        if cur_sum == self.target_sum:
            self.count += 1

        self.count += self.all_sums[cur_sum - self.target_sum]
        self.all_sums[cur_sum] += 1

        self.preorder(node.left, cur_sum)
        self.preorder(node.right, cur_sum)

        self.all_sums[cur_sum] -= 1
