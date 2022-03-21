from typing import List


# https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/discuss/1524312/Python-Binary-Search-O((m%2Bn)log1010)
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums1_neg = [-x for x in nums1 if x < 0][::-1]
        nums1_pos = [x for x in nums1 if x >= 0]
        nums2_neg = [-x for x in nums2 if x < 0][::-1]
        nums2_pos = [x for x in nums2 if x >= 0]

        neg = len(nums1_neg) * len(nums2_pos) + len(nums1_pos) * len(nums2_neg)

        if k > neg:
            k -= neg
            sign = 1
        else:
            k = neg - k + 1
            nums2_neg, nums2_pos = nums2_pos, nums2_neg
            sign = -1

        left, right = 0, 10 ** 10
        while left < right:
            mid = left + (right - left) // 2
            if self.count(nums1_neg, nums2_neg, mid) + self.count(nums1_pos, nums2_pos, mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left * sign

    def count(self, nums1, nums2, product_max):
        res = 0
        j = len(nums2) - 1
        for i in range(len(nums1)):
            while j >= 0 and nums1[i] * nums2[j] > product_max:
                j -= 1
            res += j + 1
        return res
