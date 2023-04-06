# https://leetcode.com/problems/minimize-maximum-of-array/solutions/2706521/java-c-python-prefix-sum-average-o-n/?orderBy=most_votes
import math


class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        pre_sum = 0
        res = 0

        for i, val in enumerate(nums):
            pre_sum += val
            res = max(res, math.ceil(pre_sum / (i + 1)))

        return res
