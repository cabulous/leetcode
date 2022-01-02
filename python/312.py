from functools import lru_cache


# DP top-down
class Solution:
    def __init__(self):
        self.nums = []

    def maxCoins(self, nums: [int]) -> int:
        if not nums:
            return 0

        self.nums = [1] + nums + [1]

        return self.helper(0, len(self.nums) - 1)

    @lru_cache(None)
    def helper(self, left, right):
        if left + 1 == right:
            return 0
        return max(
            self.nums[left] * self.nums[i] * self.nums[right] + self.helper(left, i) + self.helper(i, right)
            for i in range(left + 1, right)
        )


# DP bottom-up
class Solution:
    def maxCoins(self, nums: [int]) -> int:
        if not nums:
            return 0

        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for left in reversed(range(n - 1)):
            for right in range(left + 2, n):
                dp[left][right] = max(
                    nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right] for i in range(left + 1, right)
                )

        return dp[0][-1]
