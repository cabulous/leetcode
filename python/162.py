from typing import List


# https://leetcode.com/problems/find-peak-element/discuss/50259/My-clean-and-readable-python-solution
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left if nums[left] >= nums[right] else right


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1
