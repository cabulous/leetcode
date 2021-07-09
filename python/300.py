# DP
import bisect


class Solution:
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


# binary search
class Solution:
    def lengthOfLIS(self, nums):
        sub = []

        for num in nums:
            idx = bisect.bisect_left(sub, num)
            if idx == len(sub):
                sub.append(num)
            else:
                sub[idx] = num

        return len(sub)
