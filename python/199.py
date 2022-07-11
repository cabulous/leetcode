from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/binary-tree-right-side-view/discuss/56064/5-9-Lines-Python-48%2B-ms
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        level = [root]
        res = []

        while level:
            res.append(level[-1].val)
            level = [kid for node in level for kid in [node.left, node.right] if kid]

        return res


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue = deque([root, None, ])
        ans = []
        curr = root

        while queue:
            prev, curr = curr, queue.popleft()
            while curr:
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                prev, curr = curr, queue.popleft()
            ans.append(prev.val)
            if queue:
                queue.append(None)

        return ans
