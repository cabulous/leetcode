from typing import List


class Solution:

    def __init__(self):
        self.seen = set()
        self.grid = []
        self.rows = 0
        self.cols = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not any(grid):
            return 0

        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        return max(self.helper(r, c) for r in range(self.rows) for c in range(self.cols))

    def helper(self, r, c):
        if r < 0 or self.rows <= r or c < 0 or self.cols <= c:
            return 0

        if (r, c) in self.seen:
            return 0

        self.seen.add((r, c))

        if self.grid[r][c] == 0:
            return 0

        return 1 + self.helper(r - 1, c) + self.helper(r + 1, c) + self.helper(r, c - 1) + self.helper(r, c + 1)
