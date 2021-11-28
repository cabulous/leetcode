from typing import List


class Solution:
    def __init__(self):
        self.graph = []
        self.res = []

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.dfs(0, [0])
        return self.res

    def dfs(self, curr, path):
        if curr == len(self.graph) - 1:
            self.res.append(path)
            return
        for i in self.graph[curr]:
            self.dfs(i, path + [i])
