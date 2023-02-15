class UnionFind:

    def __init__(self):
        self._root = {}
        self.count = 0

    def find(self, x):
        if x != self._root[x]:
            self._root[x] = self.find(self._root[x])
        return self._root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self._root[root_x] = root_y
            self.count -= 1

    def contains(self, row, col):
        return (row, col) in self._root

    def add(self, row, col):
        if self.contains(row, col):
            return
        self._root[row, col] = row, col
        self.count += 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        islands = UnionFind()
        res = []

        for r, c in positions:
            islands.add(r, c)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if islands.contains(nr, nc):
                    islands.union((r, c), (nr, nc))
            res.append(islands.count)

        return res
