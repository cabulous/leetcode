class Solution:
    def isMajorityElement(self, nums: list[int], target: int) -> bool:
        if nums[len(nums) // 2] != target:
            return False

        left = self.binary_search(nums, target)
        right = self.binary_search(nums, target + 1)

        return right - left > len(nums) // 2

    def binary_search(self, nums, target):
        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left
