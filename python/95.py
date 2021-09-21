from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.helper(1, n) if n else []

    def helper(self, start, end):
        if start > end:
            return [None]

        all_trees = []

        for mid in range(start, end + 1):
            left_trees = self.helper(start, mid - 1)
            right_tress = self.helper(mid + 1, end)
            for left in left_trees:
                for right in right_tress:
                    cur = TreeNode(mid)
                    cur.left = left
                    cur.right = right
                    all_trees.append(cur)

        return all_trees
