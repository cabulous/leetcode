class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        dp = [1] * len(nums)
        counts = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        counts[i] = counts[j]
                    elif dp[i] == dp[j] + 1:
                        counts[i] += counts[j]

        max_length = max(dp)
        return sum(count for length, count in zip(dp, counts) if length == max_length)
