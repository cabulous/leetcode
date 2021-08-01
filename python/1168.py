import heapq
from typing import List
from collections import defaultdict


# Prim's Algorithm with Heap
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i, cost in enumerate(wells, 1):
            graph[0].append((cost, i))

        for house1, house2, cost in pipes:
            graph[house1].append((cost, house2))
            graph[house2].append((cost, house1))

        seen = {0}
        heapq.heapify(graph[0])
        queue = graph[0]
        res = 0

        while len(seen) < n + 1:
            cost, house = heapq.heappop(queue)
            if house not in seen:
                seen.add(house)
                res += cost
                for nei_cost, nei_house in graph[house]:
                    if nei_house not in seen:
                        heapq.heappush(queue, (nei_cost, nei_house))

        return res


# https://leetcode.com/problems/optimize-water-distribution-in-a-village/discuss/365853/C%2B%2BPythonJava-Hidden-Well-in-House-0
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        uf = {i: i for i in range(n + 1)}
        w = [[c, 0, i] for i, c in enumerate(wells, 1)]
        p = [[c, i, j] for i, j, c in pipes]

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        res = 0

        for c, x, y in sorted(w + p):
            x, y = find(x), find(y)
            if x != y:
                uf[y] = x
                res += c
                n -= 1
            if n == 0:
                return res


# Kruskal's Algorithm with Union-Find
class UnionFind:
    def __init__(self, size):
        self.parents = [i for i in range(size + 1)]
        self.rank = [0] * (size + 1)

    def find(self, x):
        if self.parents[x] == x:
            return self.parents[x]
        return self.find(self.parents[x])

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return False
        if self.rank[rootx] > self.rank[rooty]:
            self.parents[rooty] = rootx
        elif self.rank[rootx] < self.rank[rooty]:
            self.parents[rootx] = rooty
        else:
            self.parents[rooty] = rootx
            self.rank[rootx] += 1
        return True


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        ordered_edges = []

        for i, weight in enumerate(wells):
            ordered_edges.append((weight, 0, i + 1))

        for house1, house2, weight in pipes:
            ordered_edges.append((weight, house1, house2))

        ordered_edges.sort(key=lambda x: x[0])
        uf = UnionFind(n)
        total_cost = 0

        for cost, house1, house2 in ordered_edges:
            if uf.union(house1, house2):
                total_cost += cost

        return total_cost
