from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/all-possible-full-binary-trees/solutions/3804265/runtime-1ms-beats-98-7-recursion-memoization/
class Solution:

    def __init__(self):
        self.memo = {}

    def allPossibleFBT(self, n: int) -> list[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        return self.helper(n)

    def helper(self, n):
        if n in self.memo:
            return self.memo[n]

        if n == 1:
            self.memo[n] = [TreeNode()]
            return self.memo[n]

        res = []
        for i in range(1, n - 1, 2):
            left = self.helper(i)
            right = self.helper(n - i - 1)
            for left_node in left:
                for right_node in right:
                    res.append(TreeNode(0, left_node, right_node))

        self.memo[n] = res
        return self.memo[n]
