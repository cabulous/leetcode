from typing import List
from collections import defaultdict


# https://leetcode.com/problems/sum-of-distances-in-tree/solutions/130583/c-java-python-pre-order-and-post-order-dfs-o-n/
class Solution:

    def __init__(self):
        self.graph = defaultdict(set)
        self.n = 0
        self.count = []
        self.res = []

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.n = n
        self.count = [1] * n
        self.res = [0] * n
        for u, v in edges:
            self.graph[u].add(v)
            self.graph[v].add(u)

        self.dfs(0, -1)
        self.dfs2(0, -1)

        return self.res

    def dfs(self, curr, prev):
        for node in self.graph[curr]:
            if node != prev:
                self.dfs(node, curr)
                self.count[curr] += self.count[node]
                self.res[curr] += self.res[node] + self.count[node]

    def dfs2(self, curr, prev):
        for node in self.graph[curr]:
            if node != prev:
                self.res[node] = self.res[curr] - self.count[node] + (self.n - self.count[node])
                self.dfs2(node, curr)
