import bisect
from typing import List


class Solution:

    def __init__(self):
        self.nums = []

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        self.nums = nums

        lo = self.search(target)
        hi = self.search(target + 1) - 1

        return [lo, hi] if lo <= hi else [-1, -1]

    def search(self, target):
        lo, hi = 0, len(self.nums) - 1
        while lo <= hi:
            mi = lo + (hi - lo) // 2
            if self.nums[mi] < target:
                lo = mi + 1
            else:
                hi = mi - 1
        return lo


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = bisect.bisect_left(nums, target)
        hi = bisect.bisect_left(nums, target + 1) - 1
        return [lo, hi] if lo <= hi else [-1, -1]
