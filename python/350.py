from typing import List
from collections import Counter


# https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/82247/Three-Python-Solutions
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        res = []

        for n in nums2:
            if counts[n] > 0:
                res.append(n)
                counts[n] -= 1

        return res


# https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/82269/Short-Python-C%2B%2B
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list((Counter(nums1) & Counter(nums2)).elements())
