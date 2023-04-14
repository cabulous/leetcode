import copy


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        dp = copy.deepcopy(grid)
        rows = len(grid)
        cols = len(grid[0])

        for r in range(1, rows):
            dp[r][0] += dp[r - 1][0]
        for c in range(1, cols):
            dp[0][c] += dp[0][c - 1]

        for r in range(1, rows):
            for c in range(1, cols):
                dp[r][c] += min(dp[r - 1][c], dp[r][c - 1])

        return dp[-1][-1]
