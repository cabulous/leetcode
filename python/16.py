import math
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        diff = math.inf
        for i in range(len(nums)):
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]
                if abs(target - total) < abs(diff):
                    diff = target - total
                if diff == 0:
                    return target
                if total < target:
                    lo += 1
                else:
                    hi -= 1

        return target - diff
