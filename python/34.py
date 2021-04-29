import bisect
from typing import List


# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14707/9-11-lines-O(log-n)

#  Divide and Conquer with early breaks
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        def search(lo, hi):
            if nums[lo] == target == nums[hi]:
                return [lo, hi]
            if nums[lo] <= target <= nums[hi]:
                mi = lo + (hi - lo) // 2
                l, r = search(lo, mi), search(mi + 1, hi)
                return max(l, r) if -1 in l + r else [l[0], r[1]]
            return [-1, -1]

        return search(0, len(nums) - 1)


# Two binary searches
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(n):
            lo, hi = 0, len(nums)
            while lo < hi:
                mi = lo + (hi - lo) // 2
                if nums[mi] < n:
                    lo = mi + 1
                else:
                    hi = mi
            return lo

        lo = search(target)
        return [lo, search(target + 1) - 1] if target in nums[lo:lo + 1] else [-1, -1]


# Two binary searches, using the library
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = bisect.bisect_left(nums, target)
        return [lo, bisect.bisect(nums, target) - 1] if target in nums[lo: lo + 1] else [-1, -1]
