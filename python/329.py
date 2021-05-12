from typing import List


# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/78334/Python-solution-memoization-dp-288ms
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        max_row, max_col = len(matrix), len(matrix[0])
        dp = [[0] * max_col for _ in range(max_row)]

        def dfs(row, col):
            if not dp[row][col]:
                val = matrix[row][col]
                dp[row][col] = 1 + max(
                    dfs(row + 1, col) if row < max_row - 1 and matrix[row + 1][col] > val else 0,
                    dfs(row - 1, col) if row > 0 and matrix[row - 1][col] > val else 0,
                    dfs(row, col + 1) if col < max_col - 1 and matrix[row][col + 1] > val else 0,
                    dfs(row, col - 1) if col > 0 and matrix[row][col - 1] > val else 0,
                )
            return dp[row][col]

        return max(dfs(row, col) for col in range(max_col) for row in range(max_row))
