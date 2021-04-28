from typing import List


# https://leetcode.com/problems/unique-paths-ii/discuss/23410/Python-different-solutions-(O(m*n)-O(n)-in-place).

# O(n) space
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0

        r, c = len(obstacleGrid), len(obstacleGrid[0])
        cur = [0] * c
        cur[0] = 1 - obstacleGrid[0][0]

        for i in range(1, c):
            cur[i] = cur[i - 1] * (1 - obstacleGrid[0][i])
        for i in range(1, r):
            cur[0] *= (1 - obstacleGrid[i][0])
            for j in range(1, c):
                cur[j] = (cur[j - 1] + cur[j]) * (1 - obstacleGrid[i][j])

        return cur[-1]


# O(m*n) space
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0

        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * c for _ in range(r)]
        dp[0][0] = 1 - obstacleGrid[0][0]

        for i in range(1, r):
            dp[i][0] = dp[i - 1][0] * (1 - obstacleGrid[i][0])
        for i in range(1, c):
            dp[0][i] = dp[0][i - 1] * (1 - obstacleGrid[0][i])
        for i in range(1, r):
            for j in range(1, c):
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) * (1 - obstacleGrid[i][j])

        return dp[-1][-1]
