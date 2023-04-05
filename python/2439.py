# https://leetcode.com/problems/minimize-maximum-of-array/solutions/2706521/java-c-python-prefix-sum-average-o-n/?orderBy=most_votes
import math


class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        prefix_sum = 0
        res = 0

        for i, val in enumerate(nums):
            prefix_sum += val
            res = max(res, math.ceil(prefix_sum / (i + 1)))

        return res
