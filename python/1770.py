from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        dp = [[0] * (len(multipliers) + 1) for _ in range(len(multipliers) + 1)]

        for op in range(len(multipliers) - 1, -1, -1):
            for left in range(op, -1, -1):
                right = len(nums) - 1 - (op - left)
                dp[op][left] = max(
                    multipliers[op] * nums[left] + dp[op + 1][left + 1],
                    multipliers[op] * nums[right] + dp[op + 1][left],
                )

        return dp[0][0]
