class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1 - set2), list(set2 - set1)]


class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        distinct1 = []
        for num in nums1_set:
            if num not in nums2_set:
                distinct1.append(num)

        distinct2 = []
        for num in nums2_set:
            if num not in nums1_set:
                distinct2.append(num)

        return [distinct1, distinct2]
