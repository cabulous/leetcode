from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)

        while lo < hi:
            mi = lo + (hi - lo) // 2
            if nums[mi] == target:
                return mi
            if nums[mi] < target:
                lo = mi + 1
            else:
                hi = mi

        return lo
