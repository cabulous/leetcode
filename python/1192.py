from typing import List
from collections import defaultdict


# https://leetcode.com/problems/critical-connections-in-a-network/discuss/410345/Python-(98-Time-100-Memory)-clean-solution-with-explanaions-for-confused-people-like-me/419605
class Solution:

    def __init__(self):
        self.low = []
        self.edges = defaultdict(list)

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.low = [0] * n

        for u, v in connections:
            self.edges[u].append(v)
            self.edges[v].append(u)

        return self.dfs(1, 0, -1)

    def dfs(self, rank, curr, prev):
        self.low[curr] = rank
        res = []

        for node in self.edges[curr]:
            if node == prev:
                continue

            if self.low[node] == 0:
                res += self.dfs(rank + 1, node, curr)

            self.low[curr] = min(self.low[curr], self.low[node])

            if self.low[node] >= rank + 1:
                res.append([curr, node])

        return res
