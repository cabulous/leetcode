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
    def distanceLimitedPathsExist(self, n: int, edgeList: list[list[int]], queries: list[list[int]]) -> list[bool]:
        uf = UnionFind(n)
        sorted_edges = sorted((dist, u, v) for u, v, dist in edgeList)
        sorted_queries = sorted((max_dist, p, q, i) for i, (p, q, max_dist) in enumerate(queries))

        res = [False] * len(sorted_queries)
        i = 0
        for max_dist, p, q, idx in sorted_queries:
            while i < len(sorted_edges) and sorted_edges[i][0] < max_dist:
                __, u, v = sorted_edges[i]
                uf.union(u, v)
                i += 1
            res[idx] = uf.find(p) == uf.find(q)

        return res
