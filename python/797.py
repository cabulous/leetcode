from typing import List


class Solution:

    def __init__(self):
        self.graph = []
        self.res = []

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.dfs(0, [0])
        return self.res

    def dfs(self, node, path):
        if node == len(self.graph) - 1:
            self.res.append(path)
            return
        for next_node in self.graph[node]:
            self.dfs(next_node, path + [next_node])
