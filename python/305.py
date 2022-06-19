from typing import List


# https://leetcode.com/problems/number-of-islands-ii/discuss/75459/JavaPython-clear-solution-with-UnionFind-Class-(Weighting-and-Path-compression)
class UnionFind:

    def __init__(self):
        self.parent = {}
        self.count = 0

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            self.parent[x_root] = y_root
            self.count -= 1

    def contains(self, row, col):
        return (row, col) in self.parent

    def add(self, row, col):
        if self.contains(row, col):
            return
        self.parent[row, col] = (row, col)
        self.count += 1

    def get_count(self):
        return self.count


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        islands = UnionFind()
        res = []

        for row, col in positions:
            islands.add(row, col)
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if islands.contains(new_row, new_col):
                    islands.union((row, col), (new_row, new_col))
            res.append(islands.get_count())

        return res