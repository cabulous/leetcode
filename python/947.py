from collections import defaultdict
from typing import List


# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/solutions/2812641/python3-dfs-bfs-union-find-explained/
class Solution:

    def __init__(self):
        self.graph_x = defaultdict(list)
        self.graph_y = defaultdict(list)
        self.visited = set()

    def removeStones(self, stones: List[List[int]]) -> int:
        for x, y in stones:
            self.graph_x[x].append(y)
            self.graph_y[y].append(x)

        connected = 0
        for x, y in stones:
            if (x, y) not in self.visited:
                self.dfs(x, y)
                connected += 1

        return len(stones) - connected

    def dfs(self, x, y):
        if (x, y) not in self.visited:
            self.visited.add((x, y))
            for next_y in self.graph_x[x]:
                self.dfs(x, next_y)
            for next_x in self.graph_y[y]:
                self.dfs(next_x, y)
