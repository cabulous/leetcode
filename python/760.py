from collections import defaultdict


class Solution:
    def anagramMappings(self, nums1: list[int], nums2: list[int]) -> list[int]:
        lookup = defaultdict(list)
        for i, val in enumerate(nums2):
            lookup[str(val)].append(i)

        res = []
        for val in nums1:
            res.append(lookup[str(val)].pop())

        return res
