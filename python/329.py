from typing import List


# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/78334/Python-solution-memoization-dp-288ms
class Solution:

    def __init__(self):
        self.matrix = []
        self.rows = 0
        self.cols = 0
        self.dp = []

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.dp = [[0] * self.cols for _ in range(self.rows)]

        return max(self.dfs(row, col) for col in range(self.cols) for row in range(self.rows))

    def dfs(self, row, col):
        if self.dp[row][col] != 0:
            return self.dp[row][col]

        val = self.matrix[row][col]

        self.dp[row][col] = 1 + max(
            self.dfs(row - 1, col) if 0 <= row - 1 and val < self.matrix[row - 1][col] else 0,
            self.dfs(row + 1, col) if row + 1 < self.rows and val < self.matrix[row + 1][col] else 0,
            self.dfs(row, col - 1) if 0 <= col - 1 and val < self.matrix[row][col - 1] else 0,
            self.dfs(row, col + 1) if col + 1 < self.cols and val < self.matrix[row][col + 1] else 0,
        )

        return self.dp[row][col]
