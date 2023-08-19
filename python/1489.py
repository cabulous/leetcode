# https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/solutions/3929059/beats-100-js-java-c-c-python-python3-kotlin/
class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_x] = root_y


class Solution:

    def __init__(self):
        self.n = 0
        self.edges = []

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        self.n = n
        self.edges = [(u, v, w, i) for i, (u, v, w) in enumerate(edges)]
        self.edges.sort(key=lambda x: x[2])

        mst_wt = self.get_weight(-1, -1)

        critical = []
        pseudo_critical = []
        for i in range(len(self.edges)):
            if mst_wt < self.get_weight(i, -1):
                critical.append(self.edges[i][3])
            elif mst_wt == self.get_weight(-1, i):
                pseudo_critical.append(self.edges[i][3])

        return [critical, pseudo_critical]

    def get_weight(self, idx_to_exclude, idx_to_include):
        uf = UnionFind(self.n)
        res = 0

        if idx_to_include != -1:
            u, v, w, __ = self.edges[idx_to_include]
            res += w
            uf.union(u, v)

        for i in range(len(self.edges)):
            if i == idx_to_exclude:
                continue
            u, v, w, __ = self.edges[i]
            if uf.find(u) == uf.find(v):
                continue
            uf.union(u, v)
            res += w

        root = uf.find(0)
        for i in range(self.n):
            if uf.find(i) != root:
                return float('inf')

        return res
