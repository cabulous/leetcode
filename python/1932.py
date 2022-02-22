from collections import defaultdict
from typing import List, Optional


# https://leetcode.com/problems/merge-bsts-to-create-single-bst/discuss/1330156/Python-clean-in-order-traversal-solution-O(N)-O(N)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.nodes = {}
        self.in_degree = defaultdict(int)
        self.seen = set()
        self.is_invalid = False
        self.sub_root_val = float('-inf')

    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        self.collect_nodes(trees)

        root_vals = [val for val, in_degree_count in self.in_degree.items() if in_degree_count == 0]
        if len(root_vals) != 1:
            return None

        root = self.inorder(root_vals[0])

        if self.is_invalid or len(self.seen) != len(self.nodes):
            return None

        return root

    def inorder(self, val):
        if val in self.seen:
            self.is_invalid = True
            return

        self.seen.add(val)
        node = self.nodes[val]

        if node.left:
            node.left = self.inorder(node.left.val)

        if val <= self.sub_root_val:
            self.is_invalid = True
            return

        self.sub_root_val = val

        if node.right:
            node.right = self.inorder(node.right.val)

        return node

    def collect_nodes(self, trees):
        for tree in trees:
            if tree.val not in self.in_degree:
                self.in_degree[tree.val] = 0
            if tree.left:
                self.in_degree[tree.left.val] += 1
                if tree.left.val not in self.nodes:
                    self.nodes[tree.left.val] = tree.left
            if tree.right:
                self.in_degree[tree.right.val] += 1
                if tree.right.val not in self.nodes:
                    self.nodes[tree.right.val] = tree.right
            self.nodes[tree.val] = tree
