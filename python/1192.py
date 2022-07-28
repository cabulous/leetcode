from typing import List
from collections import defaultdict


# https://leetcode.com/problems/critical-connections-in-a-network/discuss/601695/Cleanest-and-Easiest-Understand-Python-Solution-99-Time-100-Mem
class Solution:

    def __init__(self):
        self.graph = defaultdict(list)
        self.depth = []
        self.res = []

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        for u, v in connections:
            self.graph[u].append(v)
            self.graph[v].append(u)

        self.depth = [-1] * n
        self.dfs(None, 0, 0)

        return self.res

    def dfs(self, prev_node, curr_node, curr_depth):
        self.depth[curr_node] = curr_depth
        min_depth = curr_depth

        for next_node in self.graph[curr_node]:
            if next_node == prev_node:
                continue

            next_depth = self.depth[next_node]
            if next_depth == -1:
                next_depth = self.dfs(curr_node, next_node, curr_depth + 1)

            if next_depth > curr_depth:
                self.res.append([curr_node, next_node])
            else:
                min_depth = min(min_depth, next_depth)

        self.depth[curr_node] = min_depth

        return min_depth
