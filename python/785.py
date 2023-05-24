from typing import List


# https://leetcode.com/problems/is-graph-bipartite/discuss/115543/Easy-Python-Solution/800016
class Solution:

    def __init__(self):
        self.memo = {}
        self.graph = []

    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.graph = graph
        return all(node in self.memo or self.can_bipartite(node, 1) for node in range(len(graph)))

    def can_bipartite(self, node, color):
        if node in self.memo:
            return self.memo[node] == color

        self.memo[node] = color

        for next_node in self.graph[node]:
            if not self.can_bipartite(next_node, -color):
                return False

        return True
