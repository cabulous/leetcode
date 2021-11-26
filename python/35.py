from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mi = lo + (hi - lo) // 2
            if nums[mi] == target:
                return mi
            if nums[mi] < target:
                lo = mi + 1
            else:
                hi = mi - 1

        return lo
