import math
from typing import List


# https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/discuss/489743/JavaC%2B%2BPython-One-Pass-O(1)-Space
class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        min_peak = math.inf
        max_valley = -math.inf
        total = 0
        improve = 0

        for a, b in zip(nums, nums[1:]):
            total += abs(a - b)
            improve = max(improve, abs(nums[0] - b) - abs(a - b))
            improve = max(improve, abs(nums[-1] - a) - abs(a - b))
            min_peak = min(min_peak, max(a, b))
            max_valley = max(max_valley, min(a, b))

        return total + max(improve, (max_valley - min_peak) * 2)
