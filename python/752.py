from typing import List
from collections import deque


# bfs
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
            for i in range(4):
                num = int(node[i])
                for d in [-1, 1]:
                    new_num = (num + d) % 10
                    yield node[:i] + str(new_num) + node[i + 1:]

        dead = set(deadends)
        queue = deque([('0000', 0)])
        seen = {'0000'}

        while queue:
            node, steps = queue.popleft()
            if node == target:
                return steps
            if node in dead:
                continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, steps + 1))

        return -1
