from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not any(triangle):
            return 0

        dp = triangle[-1]

        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                dp[col] = min(dp[col], dp[col + 1]) + triangle[row][col]

        return dp[0]
