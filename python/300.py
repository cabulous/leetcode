import bisect


class Solution:
    def lengthOfLIS(self, nums):
        res = []

        for num in nums:
            idx = bisect.bisect_left(res, num)
            if idx == len(res):
                res.append(num)
            else:
                res[idx] = num

        return len(res)


class Solution:
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)

        for end in range(1, len(nums)):
            for start in range(end):
                if nums[start] < nums[end]:
                    dp[end] = max(dp[end], dp[start] + 1)

        return max(dp)
