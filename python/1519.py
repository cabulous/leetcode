from collections import defaultdict, Counter
from typing import List


class Solution:

    def __init__(self):
        self.labels = ''
        self.graph = defaultdict(list)
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

        for next_node in self.graph[curr]:
            if next_node != prev:
                count += self.dfs(next_node, curr)

        count[self.labels[curr]] += 1
        self.res[curr] = count[self.labels[curr]]

        return count
