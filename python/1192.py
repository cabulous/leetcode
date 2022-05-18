from typing import List
from collections import defaultdict


# https://leetcode.com/problems/critical-connections-in-a-network/discuss/410345/Python-(98-Time-100-Memory)-clean-solution-with-explanaions-for-confused-people-like-me/419605
class Solution:

    def __init__(self):
        self.rank_min = []
        self.graph = defaultdict(list)

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.rank_min = [0] * n

        for u, v in connections:
            self.graph[u].append(v)
            self.graph[v].append(u)

        return self.dfs(1, 0, -1)

    def dfs(self, rank, curr_node, prev_node):
        self.rank_min[curr_node] = rank
        res = []

        for next_node in self.graph[curr_node]:
            if next_node == prev_node:
                continue

            if self.rank_min[next_node] == 0:
                res += self.dfs(rank + 1, next_node, curr_node)

            self.rank_min[curr_node] = min(self.rank_min[curr_node], self.rank_min[next_node])

            if self.rank_min[next_node] >= rank + 1:
                res.append([curr_node, next_node])

        return res
