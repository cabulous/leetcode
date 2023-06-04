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

    def add(self, val: int):
        self.binary_add(self.root, val)

    def binary_add(self, node: Optional[TreeNode], val: int) -> TreeNode:
        if node is None:
            return TreeNode(val)
        if val == node.val:
            return node
        if val < node.val:
            node.left = self.binary_add(node.left, val)
        else:
            node.right = self.binary_add(node.right, val)
        return node

    def remove(self, val: int):
        self.binary_remove(self.root, val)

    def binary_remove(self, node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if node is None:
            return None
        if val < node.val:
            node.left = self.binary_remove(node.left, val)
        elif val > node.val:
            node.right = self.binary_remove(node.right, val)
        else:
            if node.left is None and node.right is None:
                node = None
            elif node.left is None:
                node.val = self.successor(node)
                node.right = self.binary_remove(node.right, node.val)
            else:
                node.val = self.predecessor(node)
                node.left = self.binary_remove(node.left, node.val)
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


class Bucket:

    def __init__(self):
        self.tree = BinarySearchTree()

    def add(self, val: int):
        self.tree.add(val)

    def remove(self, val: int):
        self.tree.remove(val)

    def contains(self, val: int) -> bool:
        return self.tree.search(val) is not None


class MyHashSet:

    def __init__(self):
        self.key_range = 769
        self.data = [Bucket() for _ in range(self.key_range)]

    def _hash_key(self, key: int) -> int:
        return key % self.key_range

    def add(self, key: int) -> None:
        idx = self._hash_key(key)
        self.data[idx].add(key)

    def remove(self, key: int) -> None:
        idx = self._hash_key(key)
        self.data[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self._hash_key(key)
        return self.data[idx].contains(key)
