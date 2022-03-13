from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:

    def __init__(self):
        self.memo = {}

    def cloneGraph(self, node: Node) -> Optional[Node]:
        if node is None:
            return None

        if node in self.memo:
            return self.memo[node]

        clone = Node(node.val)
        self.memo[node] = clone

        if node.neighbors:
            clone.neighbors = [self.cloneGraph(nei) for nei in node.neighbors]

        return clone


class Solution:
    def cloneGraph(self, node: Node) -> Optional[Node]:
        if node is None:
            return None

        queue = deque([node])
        clone = {node: Node(node.val)}

        while queue:
            curr_node = queue.popleft()
            for nei in curr_node.neighbors:
                if nei not in clone:
                    clone[nei] = Node(nei.val)
                    queue.append(nei)
                clone[curr_node].neighbors.append(clone[nei])

        return clone[node]
