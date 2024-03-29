class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [0] * cols
        dp[0] = 1 - obstacleGrid[0][0]

        for c in range(1, cols):
            dp[c] = dp[c - 1] * (1 - obstacleGrid[0][c])

        for r in range(1, rows):
            dp[0] = dp[0] * (1 - obstacleGrid[r][0])
            for c in range(1, cols):
                dp[c] = (dp[c] + dp[c - 1]) * (1 - obstacleGrid[r][c])

        return dp[-1]
