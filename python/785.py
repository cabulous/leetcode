from typing import List
from collections import deque


# https://leetcode.com/problems/is-graph-bipartite/discuss/115543/Easy-Python-Solution/800016
class Solution:

    def __init__(self):
        self.color_memo = {}
        self.graph = []

    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.graph = graph
        return all(i in self.color_memo or self.can_bipartite(i, 1) for i in range(len(graph)))

    def can_bipartite(self, node, color):
        if node in self.color_memo:
            return self.color_memo[node] == color

        self.color_memo[node] = color

        return all(self.can_bipartite(next_node, -color) for next_node in self.graph[node])
