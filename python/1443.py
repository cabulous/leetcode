from collections import defaultdict
from typing import List


class Solution:

    def __init__(self):
        self.has_apple = []
        self.graph = defaultdict(list)
        self.res = []

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.has_apple = hasApple
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
        return max(0, self.dfs(0, -1) - 2)

    def dfs(self, curr, prev):
        res = 0

        for node in self.graph[curr]:
            if node != prev:
                res += self.dfs(node, curr)

        if res or self.has_apple[curr]:
            return res + 2

        return res
