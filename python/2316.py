from collections import Counter


class UnionFind:

    def __init__(self, size):
        self.root = list(range(size))

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_x] = root_y


class Solution:
    def countPairs(self, n: int, edges: list[list[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)

        group_sizes = list(Counter(uf.find(i) for i in range(n)).values())
        curr_size = group_sizes[0]
        res = 0

        for size in group_sizes[1:]:
            res += curr_size * size
            curr_size += size

        return res
