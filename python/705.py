from typing import Optional


class TreeNode:

    def __init__(self, val=-1):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = TreeNode()

    def search(self, val: int) -> Optional[TreeNode]:
        return self.binary_search(self.root, val)

    def binary_search(self, node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if node is None:
            return None
        if val == node.val:
            return node
        if val < node.val:
            return self.binary_search(node.left, val)
        return self.binary_search(node.right, val)

    def insert(self, val: int):
        self.binary_insert(self.root, val)

    def binary_insert(self, node: Optional[TreeNode], val: int) -> TreeNode:
        if node is None:
            return TreeNode(val)
        if val == node.val:
            return node
        if val < node.val:
            node.left = self.binary_insert(node.left, val)
        else:
            node.right = self.binary_insert(node.right, val)
        return node

    def successor(self, node: TreeNode) -> int:
        node = node.right
        while node.left:
            node = node.left
        return node.val

    def predecessor(self, node: TreeNode) -> int:
        node = node.left
        while node.right:
            node = node.right
        return node.val

    def delete(self, val: int) -> Optional[TreeNode]:
        return self.binary_delete(self.root, val)

    def binary_delete(self, node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if node is None:
            return None

        if val < node.val:
            node.left = self.binary_delete(node.left, val)
        elif val > node.val:
            node.right = self.binary_delete(node.right, val)
        else:
            if node.left is None and node.right is None:
                node = None
            elif node.left is None:
                node.val = self.successor(node)
                node.right = self.binary_delete(node.right, node.val)
            else:
                node.val = self.predecessor(node)
                node.left = self.binary_delete(node.left, node.val)

        return node


class Bucket:

    def __init__(self):
        self.tree = BinarySearchTree()

    def insert(self, val):
        self.tree.insert(val)

    def delete(self, val):
        self.tree.delete(val)

    def exits(self, val):
        return self.tree.search(val) is not None


class MyHashSet:

    def __init__(self):
        self.key_range = 769
        self.data = [Bucket() for _ in range(self.key_range)]

    def hash(self, key: int) -> int:
        return key % self.key_range

    def add(self, key: int) -> None:
        index = self.hash(key)
        return self.data[index].insert(key)

    def remove(self, key: int) -> None:
        index = self.hash(key)
        return self.data[index].delete(key)

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        return self.data[index].exits(key)
