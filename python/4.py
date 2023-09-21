# https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2511/Intuitive-Python-O(log-(m%2Bn))-solution-by-kth-smallest-in-the-two-sorted-arrays-252ms
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        total_len = len(nums1) + len(nums2)

        if total_len % 2 == 1:
            return self.kth(nums1, nums2, total_len // 2)

        n1 = self.kth(nums1, nums2, total_len // 2)
        n2 = self.kth(nums1, nums2, total_len // 2 - 1)
        return (n1 + n2) / 2

    def kth(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]

        idx1, idx2 = len(nums1) // 2, len(nums2) // 2
        median1, median2 = nums1[idx1], nums2[idx2]

        if idx1 + idx2 < k:
            if median1 < median2:
                return self.kth(nums1[idx1 + 1:], nums2, k - idx1 - 1)
            return self.kth(nums1, nums2[idx2 + 1:], k - idx2 - 1)

        if median1 < median2:
            return self.kth(nums1, nums2[:idx2], k)
        return self.kth(nums1[:idx1], nums2, k)
