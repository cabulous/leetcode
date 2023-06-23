class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        dp = {}

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                diff = nums[j] - nums[i]
                dp[j, diff] = 1 + dp.get((i, diff), 1)

        return max(dp.values())
