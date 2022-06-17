class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


IS_LEAF = 0
IS_PARENT_OR_LEAF_WITH_CAMERA = 1
IS_COVERED_WITHOUT_CAMERA = 2


# https://leetcode.com/problems/binary-tree-cameras/discuss/211180/JavaC%2B%2BPython-Greedy-DFS
class Solution:

    def __init__(self):
        self.res = 0

    def minCameraCover(self, root: TreeNode) -> int:
        ret = self.dfs(root)
        return self.res + (ret == IS_LEAF)

    def dfs(self, node: TreeNode):
        if node is None:
            return IS_COVERED_WITHOUT_CAMERA

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        if left == IS_LEAF or right == IS_LEAF:
            self.res += 1
            return IS_PARENT_OR_LEAF_WITH_CAMERA

        if left == IS_PARENT_OR_LEAF_WITH_CAMERA or right == IS_PARENT_OR_LEAF_WITH_CAMERA:
            return IS_COVERED_WITHOUT_CAMERA

        return IS_LEAF
