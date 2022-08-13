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
