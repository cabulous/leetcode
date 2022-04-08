from typing import List


class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)
        res = 0
        for n1, n2 in zip(nums1, nums2):
            res += n1 * n2
        return res
