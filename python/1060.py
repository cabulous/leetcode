class Solution:

    def __init__(self):
        self.nums = []

    def missingElement(self, nums: list[int], k: int) -> int:
        self.nums = nums

        if k > self.missing(len(nums) - 1):
            return nums[-1] + k - self.missing(len(nums) - 1)

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if self.missing(mid) < k:
                left = mid + 1
            else:
                right = mid

        return nums[left - 1] + k - self.missing(left - 1)

    def missing(self, idx):
        return self.nums[idx] - self.nums[0] - idx
