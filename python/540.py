from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mi = lo + (hi - lo) // 2
            if mi % 2 == 1:
                mi -= 1
            if nums[mi] == nums[mi + 1]:
                lo = mi + 2
            else:
                hi = mi - 1

        return nums[lo]
