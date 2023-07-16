from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.graph = defaultdict(list)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        self.connect(None, root)

        queue = [target.val]
        visited = {target.val}

        for _ in range(k):
            next_queue = []
            for val in queue:
                for next_val in self.graph[val]:
                    if next_val not in visited:
                        visited.add(next_val)
                        next_queue.append(next_val)
            queue = next_queue

        return queue

    def connect(self, parent, child):
        if parent and child:
            self.graph[parent.val].append(child.val)
            self.graph[child.val].append(parent.val)
        if child.left:
            self.connect(child, child.left)
        if child.right:
            self.connect(child, child.right)
