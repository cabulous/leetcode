from itertools import product
from typing import List
from collections import defaultdict


# https://leetcode.com/problems/rank-transform-of-a-matrix/discuss/1390809/Python-greedy-Union-Find-explained
class DSU:
    def __init__(self, graph):
        self.p = {i: i for i in graph}

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        self.p[x] = y

    def groups(self):
        groups = defaultdict(list)
        for el in self.p.keys():
            groups[self.find(el)].append(el)
        return groups


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        rank = [0] * (m + n)
        d = defaultdict(list)

        for i, j in product(range(n), range(m)):
            d[matrix[i][j]].append([i, j])

        for a in sorted(d):
            graph = [i for i, j in d[a]] + [j + n for i, j in d[a]]
            dsu = DSU(graph)
            for i, j in d[a]:
                dsu.union(i, j + n)
            for group in dsu.groups().values():
                mx = max(rank[i] for i in group)
                for i in group:
                    rank[i] = mx + 1
            for i, j in d[a]:
                matrix[i][j] = rank[i]

        return matrix
