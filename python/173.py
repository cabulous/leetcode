from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.collect_leftmost(root)

    def collect_leftmost(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        curr = self.stack.pop()
        if curr.right:
            self.collect_leftmost(curr.right)
        return curr.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
