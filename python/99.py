from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        nums = self.inorder(root)
        x, y = self.find_two_swapped(nums)
        self.recover(root, 2, x, y)

    def inorder(self, node):
        return self.inorder(node.left) + [node.val] + self.inorder(node.right) if node else []

    def find_two_swapped(self, nums):
        n = len(nums)
        x = y = None

        for i in range(n - 1):
            if nums[i + 1] < nums[i]:
                y = nums[i + 1]
                if x is None:
                    x = nums[i]
                else:
                    break

        return x, y

    def recover(self, node, count, x, y):
        if node:
            if node.val == x or node.val == y:
                node.val = y if node.val == x else x
                count -= 1
                if count == 0:
                    return
            self.recover(node.left, count, x, y)
            self.recover(node.right, count, x, y)
