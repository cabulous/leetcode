import heapq
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        nums = self.inorder(root)
        nums.sort(key=lambda x: abs(x - target))
        return nums[:k]

    def inorder(self, node: TreeNode):
        return self.inorder(node.left) + [node.val] + self.inorder(node.right) if node else []


class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        queue = []

        def inorder(node: TreeNode):
            if not node:
                return
            inorder(node.left)
            heapq.heappush(queue, (-abs(node.val - target), node.val))
            if len(queue) > k:
                heapq.heappop(queue)
            inorder(node.right)

        inorder(root)
        return [x for _, x in queue]


# https://leetcode.com/problems/closest-binary-search-tree-value-ii/discuss/70534/O(k-%2B-logn)-Python-Solution
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        pre_stack = []
        suc_stack = []

        while root:
            if root.val < target:
                pre_stack.append(root)
                root = root.right
            else:
                suc_stack.append(root)
                root = root.left

        pre = self.get_predecessor(pre_stack)
        suc = self.get_successor(suc_stack)
        res = []

        while k:
            k -= 1
            if pre and not suc:
                res.append(pre.val)
                pre = self.get_predecessor(pre_stack)
            elif not pre and suc:
                res.append(suc.val)
                suc = self.get_successor(suc_stack)
            elif pre and suc and abs(pre.val - target) < abs(suc.val - target):
                res.append(pre.val)
                pre = self.get_predecessor(pre_stack)
            elif pre and suc and abs(pre.val - target) >= abs(suc.val - target):
                res.append(suc.val)
                suc = self.get_successor(suc_stack)

        return res

    def get_predecessor(self, stack: List[TreeNode]):
        if not stack:
            return None
        pre = stack.pop()
        p = pre.left
        while p:
            stack.append(p)
            p = p.right
        return pre

    def get_successor(self, stack: List[TreeNode]):
        if not stack:
            return None
        suc = stack.pop()
        p = suc.right
        while p:
            stack.append(p)
            p = p.left
        return suc
