from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/discuss/252232/JavaC%2B%2BPython-O(N)-Solution
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.build_tree(preorder[::-1], float('inf'))

    def build_tree(self, reversed_preorder, bound):
        if not reversed_preorder or reversed_preorder[-1] > bound:
            return None
        node = TreeNode(reversed_preorder.pop())
        node.left = self.build_tree(reversed_preorder, node.val)
        node.right = self.build_tree(reversed_preorder, bound)
        return node
