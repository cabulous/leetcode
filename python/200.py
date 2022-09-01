from typing import List


class Solution:

    def __init__(self):
        self.grid = []
        self.rows = 0
        self.cols = 0
        self.seen = set()

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        res = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == '1' and (r, c) not in self.seen:
                    self.helper(r, c)
                    res += 1

        return res

    def helper(self, row, col):
        if row < 0 or self.rows <= row or col < 0 or self.cols <= col:
            return
        if (row, col) in self.seen:
            return

        self.seen.add((row, col))

        if self.grid[row][col] == '0':
            return

        self.helper(row + 1, col)
        self.helper(row - 1, col)
        self.helper(row, col + 1)
        self.helper(row, col - 1)
