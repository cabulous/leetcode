from collections import defaultdict, Counter
from typing import List


class Solution:

    def __init__(self):
        self.graph = defaultdict(list)
        self.labels = []
        self.res = []

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.labels = labels
        self.res = [0] * n

        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)

        self.dfs(0, -1)

        return self.res

    def dfs(self, curr, prev):
        count = Counter()

        for node in self.graph[curr]:
            if node != prev:
                count += self.dfs(node, curr)

        count[self.labels[curr]] += 1
        self.res[curr] = count[self.labels[curr]]

        return count
