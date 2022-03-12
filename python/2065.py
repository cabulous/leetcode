from collections import defaultdict
from typing import List


# https://leetcode.com/problems/maximum-path-quality-of-a-graph/discuss/1563898/Python-Concise-DFS
class Solution:

    def __init__(self):
        self.values = []
        self.graph = defaultdict(dict)

    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        self.values = values

        for u, v, time in edges:
            self.graph[u][v] = time
            self.graph[v][u] = time

        return self.dfs(0, {0}, maxTime)

    def dfs(self, curr_node, seen, remaining_time):
        res = sum(self.values[node] for node in seen) if curr_node == 0 else 0
        for next_node in self.graph[curr_node]:
            next_time = self.graph[curr_node][next_node]
            if remaining_time >= next_time:
                res = max(res, self.dfs(next_node, seen | {next_node}, remaining_time - next_time))
        return res
