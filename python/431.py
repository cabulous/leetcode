from typing import Optional


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/discuss/151772/Python-left-child-for-children-right-child-for-siblings
class Codec:
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root:
            return None

        binary = TreeNode(root.val)
        if not root.children:
            return binary

        binary.left = self.encode(root.children[0])
        node = binary.left
        for kid in root.children[1:]:
            node.right = self.encode(kid)
            node = node.right

        return binary

    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data:
            return None

        nary = Node(data.val, [])
        node = data.left
        while node:
            nary.children.append(self.decode(node))
            node = node.right

        return nary
