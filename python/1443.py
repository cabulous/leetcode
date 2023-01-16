from collections import defaultdict
from typing import List


class Solution:

    def __init__(self):
        self.has_apple = []
        self.graph = defaultdict(list)

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.has_apple = hasApple

        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)

        return max(0, self.dfs(0, -1) - 2)

    def dfs(self, curr, prev):
        res = 0

        for next_node in self.graph[curr]:
            if next_node != prev:
                res += self.dfs(next_node, curr)

        if res != 0 or self.has_apple[curr]:
            res += 2

        return res
