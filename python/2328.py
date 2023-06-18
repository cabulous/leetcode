from functools import lru_cache

MOD = 10 ** 9 + 7


class Solution:

    def __init__(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.grid = []
        self.rows = 0
        self.cols = 0

    def countPaths(self, grid: list[list[int]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        res = (self.rows * self.cols) % MOD
        for r in range(self.rows):
            for c in range(self.cols):
                res += self.dp(r, c)
                res %= MOD

        return res

    @lru_cache(None)
    def dp(self, row, col):
        res = 0
        for dr, dc in self.directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] > self.grid[row][col]:
                res += 1 + self.dp(nr, nc)
        return res
