from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/discuss/464368/Short-O(n)-Python
class Solution:

    def __init__(self):
        self.values = []

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.collect(root1)
        self.collect(root2)
        return sorted(self.values)

    def collect(self, root: TreeNode):
        if root:
            self.collect(root.left)
            self.values.append(root.val)
            self.collect(root.right)


# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/discuss/1720210/JavaC%2B%2BPython-A-very-very-detailed-EXPLANATION
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1, stack2 = [], []
        res = []

        while root1 is not None or root2 is not None or len(stack1) > 0 or len(stack2) > 0:

            while root1 is not None:
                stack1.append(root1)
                root1 = root1.left

            while root2 is not None:
                stack2.append(root2)
                root2 = root2.left

            if len(stack2) == 0 or (len(stack1) > 0 and stack1[-1].val <= stack2[-1].val):
                root1 = stack1.pop()
                res.append(root1.val)
                root1 = root1.right
            else:
                root2 = stack2.pop()
                res.append(root2.val)
                root2 = root2.right

        return res
