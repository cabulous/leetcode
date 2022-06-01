from typing import List


# https://leetcode.com/problems/number-of-islands-ii/discuss/75459/JavaPython-clear-solution-with-UnionFind-Class-(Weighting-and-Path-compression)
class UnionFind:

    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.count = 0

    def add(self, position):
        if position in self.parent:
            return
        self.parent[position] = position
        self.rank[position] = 1
        self.count += 1

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.rank[x_root] > self.rank[y_root]:
            x_root, y_root = y_root, x_root

        self.parent[x_root] = y_root
        self.rank[y_root] += self.rank[x_root]
        self.count -= 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        islands = UnionFind()
        res = []

        for row, col in positions:
            islands.add((row, col))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dr, col + dc
                if (new_row, new_col) in islands.parent:
                    islands.union((row, col), (new_row, new_col))
            res.append(islands.count)

        return res
