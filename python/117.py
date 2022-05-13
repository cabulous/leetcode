from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return root

        level = [root]

        while level:
            for i in range(1, len(level)):
                level[i - 1].next = level[i]
            level = [kid for node in level for kid in [node.left, node.right] if kid]

        return root
