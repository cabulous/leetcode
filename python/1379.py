from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        original_queue = deque([original])
        cloned_queue = deque([cloned])

        while original_queue:
            o_node = original_queue.popleft()
            c_node = cloned_queue.popleft()

            if o_node is target:
                return c_node

            if o_node.left:
                original_queue.append(o_node.left)
                cloned_queue.append(c_node.left)
            if o_node.right:
                original_queue.append(o_node.right)
                cloned_queue.append(c_node.right)


class Solution:

    def __init__(self):
        self.target = None
        self.res = None

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.target = target
        self.inorder(original, cloned)
        return self.res

    def inorder(self, original_node, cloned_node):
        if original_node.left:
            self.inorder(original_node.left, cloned_node.left)

        if original_node is self.target:
            self.res = cloned_node
            return

        if original_node.right:
            self.inorder(original_node.right, cloned_node.right)
