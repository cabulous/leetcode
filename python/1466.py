from collections import defaultdict
from typing import List


# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/discuss/661774/Python3-Easy-Short-DFS
class Solution:

    def __init__(self):
        self.graph = defaultdict(list)
        self.roads = set()
        self.res = 0

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        for u, v in connections:
            self.roads.add((u, v))
            self.graph[u].append(v)
            self.graph[v].append(u)

        self.dfs(0, -1)

        return self.res

    def dfs(self, curr_node, prev_node):
        if (prev_node, curr_node) in self.roads:
            self.res += 1

        for next_node in self.graph[curr_node]:
            if next_node != prev_node:
                self.dfs(next_node, curr_node)
