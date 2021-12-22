from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not any(matrix):
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        res = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])
                    res = max(res, dp[i][j] ** 2)

        return res
