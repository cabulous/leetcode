from functools import lru_cache
import math


# dp dfs
class Solution:
    def cherryPickup(self, grid: [[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(row, col1, col2):
            if col1 < 0 or col1 >= n or col2 < 0 or col2 >= n:
                return -math.inf
            result = 0
            result += grid[row][col1]
            if col1 != col2:
                result += grid[row][col2]
            if row != m - 1:
                result += max(
                    dfs(row + 1, new_col1, new_col2)
                    for new_col1 in [col1 - 1, col1, col1 + 1]
                    for new_col2 in [col2 - 1, col2, col2 + 1]
                )
            return result

        return dfs(0, 0, n - 1)


# dp
class Solution:
    def cherryPickup(self, grid: [[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        dp = [[[0] * n for _ in range(n)] for _ in range(m)]

        for row in reversed(range(m)):
            for col1 in range(n):
                for col2 in range(n):
                    result = 0
                    result += grid[row][col1]
                    if col1 != col2:
                        result += grid[row][col2]
                    if row != m - 1:
                        result += max(
                            dp[row + 1][new_col1][new_col2]
                            for new_col1 in [col1 - 1, col1, col1 + 1]
                            for new_col2 in [col2 - 1, col2, col2 + 1]
                            if 0 <= new_col1 < n and 0 <= new_col2 < n
                        )
                    dp[row][col1][col2] = result

        return dp[0][0][-1]
