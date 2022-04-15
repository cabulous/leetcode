from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.last = root
        self.stack = []
        self.arr = []
        self.pointer = -1

    def hasNext(self) -> bool:
        if len(self.stack) > 0:
            return True
        if self.last is not None:
            return True
        if self.pointer < len(self.arr) - 1:
            return True
        return False

    def next(self) -> int:
        self.pointer += 1
        if self.pointer == len(self.arr):
            while self.last:
                self.stack.append(self.last)
                self.last = self.last.left
            curr = self.stack.pop()
            self.last = curr.right
            self.arr.append(curr.val)
        return self.arr[self.pointer]

    def hasPrev(self) -> bool:
        return self.pointer > 0

    def prev(self) -> int:
        self.pointer -= 1
        return self.arr[self.pointer]
