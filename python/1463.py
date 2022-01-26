from functools import lru_cache
import math


# dfs
class Solution:

    def __init__(self):
        self.grid = []
        self.rows = 0
        self.cols = 0

    def cherryPickup(self, grid: [[int]]) -> int:
        if not any(grid):
            return 0

        self.grid = grid
        self.rows, self.cols = len(grid), len(grid[0])

        return self.helper(0, 0, self.cols - 1)

    @lru_cache(None)
    def helper(self, row, col1, col2):
        if col1 < 0 or self.cols <= col1 or col2 < 0 or self.cols <= col2:
            return -math.inf

        res = self.grid[row][col1]

        if col1 != col2:
            res += self.grid[row][col2]

        if row != self.rows - 1:
            res += max(
                self.helper(row + 1, new_col1, new_col2)
                for new_col1 in [col1 - 1, col1, col1 + 1]
                for new_col2 in [col2 - 1, col2, col2 + 1]
            )

        return res


# dp
class Solution:
    def cherryPickup(self, grid: [[int]]) -> int:
        if not any(grid):
            return 0

        rows, cols = len(grid), len(grid[0])
        dp = [[[0] * cols for _ in range(cols)] for _ in range(rows)]

        for r in reversed(range(rows)):
            for c1 in range(cols):
                for c2 in range(cols):
                    res = grid[r][c1]
                    if c1 != c2:
                        res += grid[r][c2]
                    if r != rows - 1:
                        res += max(
                            dp[r + 1][nc1][nc2]
                            for nc1 in [c1 - 1, c1, c1 + 1]
                            for nc2 in [c2 - 1, c2, c2 + 1]
                            if 0 <= nc1 < cols and 0 <= nc2 < cols
                        )
                    dp[r][c1][c2] = res

        return dp[0][0][-1]
