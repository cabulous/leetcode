from typing import List
from collections import defaultdict


# dfs
class Solution:
    def __init__(self):
        self.graph = defaultdict(list)

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        for u, v in edges:
            seen = set()
            if u in self.graph and v in self.graph and self.dfs(u, v, seen):
                return [u, v]
            self.graph[u].append(v)
            self.graph[v].append(u)

    def dfs(self, source, target, seen):
        if source in seen:
            return False
        if source == target:
            return True
        seen.add(source)
        return any(self.dfs(nei, target, seen) for nei in self.graph[source])


# union-find
# https://leetcode.com/problems/redundant-connection/discuss/123819/Union-Find-with-Explanations-(Java-Python)
class Solution:
    def __init__(self):
        self.parent = []

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parent = [0] * (len(edges) + 1)

        for u, v in edges:
            if not self.union(u, v):
                return [u, v]

    def find(self, x):
        if self.parent[x] == 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return False
        self.parent[rootx] = rooty
        return True
