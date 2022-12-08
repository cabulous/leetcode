from typing import List


class UnionFind:

    def __init__(self, size):
        self.root = list(range(size))
        self.count = size

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            for i in range(len(self.root)):
                if self.root[i] == root_y:
                    self.root[i] = root_x
            self.count -= 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def union_count(self):
        return self.count


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for x, y in edges:
            if not uf.connected(x, y):
                uf.union(x, y)
        return uf.union_count()
