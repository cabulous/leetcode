import math
from collections import defaultdict, Counter
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
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        lookup = defaultdict(set)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            lookup[vals[u]].add(u)
            lookup[vals[v]].add(v)

        uf = UnionFind(len(vals))
        res = len(vals)

        for val in sorted(lookup.keys()):
            for node in lookup[val]:
                for next_node in graph[node]:
                    if vals[next_node] <= val:
                        uf.union(next_node, node)

            group = Counter()
            for node in lookup[val]:
                group[uf.find(node)] += 1

            for count in group.values():
                res += math.comb(count, 2)

        return res
