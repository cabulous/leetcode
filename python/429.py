from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []

        res = []
        level = [root]
        while level:
            res.append([node.val for node in level])
            level = [kid for node in level for kid in node.children if kid]

        return res
