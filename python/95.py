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

        for i in range(start, end + 1):
            left_trees = self.helper(start, i - 1)
            right_trees = self.helper(i + 1, end)
            for l in left_trees:
                for r in right_trees:
                    cur_tree = TreeNode(i)
                    cur_tree.left = l
                    cur_tree.right = r
                    all_trees.append(cur_tree)

        return all_trees
