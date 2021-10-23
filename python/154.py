from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            pivot = lo + (hi - lo) // 2
            if nums[pivot] < nums[hi]:
                hi = pivot
            elif nums[pivot] > nums[hi]:
                lo = pivot + 1
            else:
                hi -= 1

        return nums[lo]
