from functools import lru_cache


# DP top-down
class Solution:
    def maxCoins(self, nums: [int]) -> int:
        if not nums:
            return 0
        nums = [1] + nums + [1]
        n = len(nums)

        @lru_cache(None)
        def dp(left, right):
            if left + 1 == right:
                return 0
            return max(nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right) for i in range(left + 1, right))

        return dp(0, n - 1)


# DP bottom-up
class Solution:
    def maxCoins(self, nums: [int]) -> int:
        if not nums:
            return 0
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for left in range(n - 2, -1, -1):
            for right in range(left + 2, n):
                dp[left][right] = max(
                    nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right] for i in range(left + 1, right)
                )

        return dp[0][n - 1]
