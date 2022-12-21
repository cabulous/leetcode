from collections import defaultdict, deque
from typing import List


class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_x] = root_y


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        uf = UnionFind(n + 1)

        for node in range(1, n + 1):
            for nei in graph[node]:
                if uf.find(node) == uf.find(nei):
                    return False
                uf.union(graph[node][0], nei)

        return True


class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.color = []

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        for u, v in dislikes:
            self.graph[u].append(v)
            self.graph[v].append(u)

        self.color = [-1] * (n + 1)

        for node in range(1, n + 1):
            if self.color[node] == -1:
                if not self.bfs(node):
                    return False

        return True

    def bfs(self, source):
        queue = deque([source])
        self.color[source] = 0
        while queue:
            node = queue.popleft()
            for nei in self.graph[node]:
                if self.color[node] == self.color[nei]:
                    return False
                if self.color[nei] == -1:
                    self.color[nei] = 1 - self.color[node]
                    queue.append(nei)
        return True
