class Solution:
    def isMajorityElement(self, nums: list[int], target: int) -> bool:
        if nums[len(nums) // 2] != target:
            return False

        lo = self.binary_search(nums, target)
        hi = self.binary_search(nums, target + 1)

        return hi - lo > len(nums) // 2

    def binary_search(self, nums, target):
        lo = 0
        hi = len(nums)
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if nums[mi] < target:
                lo = mi + 1
            else:
                hi = mi
        return lo
