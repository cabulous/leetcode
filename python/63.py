from typing import List


# https://leetcode.com/problems/unique-paths-ii/discuss/23410/Python-different-solutions-(O(m*n)-O(n)-in-place).
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [0] * cols
        dp[0] = 1 - obstacleGrid[0][0]

        for i in range(1, cols):
            dp[i] = dp[i - 1] * (1 - obstacleGrid[0][i])

        for i in range(1, rows):
            dp[0] *= 1 - obstacleGrid[i][0]
            for j in range(1, cols):
                dp[j] = (dp[j] + dp[j - 1]) * (1 - obstacleGrid[i][j])

        return dp[-1]
