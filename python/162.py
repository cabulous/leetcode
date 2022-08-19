from typing import List


# https://leetcode.com/problems/find-peak-element/discuss/50259/My-clean-and-readable-python-solution
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if nums[mi - 1] < nums[mi] > nums[mi + 1]:
                return mi
            if nums[mi] < nums[mi + 1]:
                lo = mi + 1
            else:
                hi = mi

        return lo if nums[lo] > nums[hi] else hi


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1
