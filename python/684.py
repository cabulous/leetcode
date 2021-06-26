from typing import List
from collections import defaultdict


# dfs
class Solution:
    def __init__(self):
        self.graph = defaultdict(list)

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        for u, v in edges:
            if u in self.graph and v in self.graph and self.reachable(u, v, set()):
                return [u, v]
            self.graph[u].append(v)
            self.graph[v].append(u)

    def reachable(self, source, target, seen):
        if source in seen:
            return False
        if source == target:
            return True
        seen.add(source)
        return any(self.reachable(nei, target, seen) for nei in self.graph[source])


# union-find
# https://leetcode.com/problems/redundant-connection/discuss/123819/Union-Find-with-Explanations-(Java-Python)
class Solution:
    def __init__(self):
        self.parent = []

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parent = [i for i in range(len(edges) + 1)]

        for u, v in edges:
            if not self.union(u, v):
                return [u, v]

    def find(self, x):
        root = self.parent[x]
        if root == x:
            return root
        root = self.find(self.parent[root])
        return root

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return False
        self.parent[rooty] = rootx
        return True
