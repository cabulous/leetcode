from typing import List

import bisect
import math


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        return self.increasing_k_nums(nums, 3)

    def increasing_k_nums(self, nums, k):
        if k == 0:
            return True

        inc = [math.inf] * (k - 1)

        for num in nums:
            idx = bisect.bisect_left(inc, num)
            if idx == k - 1:
                return True
            inc[idx] = num

        return False


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = math.inf
        second = math.inf

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False
