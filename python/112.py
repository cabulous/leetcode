from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        targetSum -= root.val

        if root.left is None and root.right is None:
            return targetSum == 0

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        queue = deque([(root, targetSum - root.val)])

        while queue:
            node, remaining = queue.popleft()
            if node.left is None and node.right is None and remaining == 0:
                return True

            if node.left:
                queue.append((node.left, remaining - node.left.val))
            if node.right:
                queue.append((node.right, remaining - node.right.val))

        return False
