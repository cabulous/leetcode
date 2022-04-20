from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.leftmost_inorder(root)

    def leftmost_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        curr = self.stack.pop()
        if curr.right:
            self.leftmost_inorder(curr.right)
        return curr.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
