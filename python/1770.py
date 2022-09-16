from functools import lru_cache
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        dp = [[0] * (len(multipliers) + 1) for _ in range(len(multipliers) + 1)]

        for op in range(len(multipliers) - 1, -1, -1):
            for left in range(op, -1, -1):
                dp[op][left] = max(
                    multipliers[op] * nums[left] + dp[op + 1][left + 1],
                    multipliers[op] * nums[len(nums) - 1 - (op - left)] + dp[op + 1][left],
                )

        return dp[0][0]


# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/discuss/1075469/JavaC%2B%2BPython-3-Top-Down-DP-O(m2)-Clean-and-Concise
class Solution:

    def __init__(self):
        self.nums = []
        self.multipliers = []

    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        self.nums = nums
        self.multipliers = multipliers
        return self.dp(0, 0)

    @lru_cache(None)
    def dp(self, left, index):
        if index == len(self.multipliers):
            return 0

        pick_left = self.dp(left + 1, index + 1) + self.nums[left] * self.multipliers[index]
        pick_right = self.dp(left, index + 1) + self.nums[len(self.nums) - (index - left) - 1] * self.multipliers[index]

        return max(pick_left, pick_right)
