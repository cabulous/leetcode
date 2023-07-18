# https://leetcode.com/problems/last-day-where-you-can-still-cross/solutions/1403930/python-union-find-solution-explained/
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

    def __init__(self):
        self.rows = 0
        self.cols = 0

    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        self.rows = row
        self.cols = col

        uf = UnionFind(row * col + 2)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        grid = [[1] * col for _ in range(row)]
        zero_indexed_cells = [(r - 1, c - 1) for r, c in cells]

        for i in range(len(zero_indexed_cells) - 1, -1, -1):
            r, c = zero_indexed_cells[i]
            grid[r][c] = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                    uf.union(self.index(nr, nc), self.index(r, c))
            if r == 0:
                uf.union(0, self.index(r, c))
            if r == row - 1:
                uf.union(row * col + 1, self.index(r, c))
            if uf.find(0) == uf.find(row * col + 1):
                return i

        return -1

    def index(self, row, col):
        return row * self.cols + col
