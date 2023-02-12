import math
from collections import defaultdict


class Solution:

    def __init__(self):
        self.graph = defaultdict(list)
        self.seats = 0
        self.res = 0

    def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:
        for u, v in roads:
            self.graph[u].append(v)
            self.graph[v].append(u)

        self.seats = seats
        self.dfs(0, -1)
        return self.res

    def dfs(self, node, prev_node):
        people = 1

        for next_node in self.graph[node]:
            if next_node != prev_node:
                people += self.dfs(next_node, node)

        if node > 0:
            self.res += math.ceil(people / self.seats)

        return people
