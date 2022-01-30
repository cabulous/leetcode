from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums_count = len(nums)
        new_nums = [0] * nums_count

        for i in range(nums_count):
            new_nums[(i + k) % nums_count] = nums[i]

        nums[:] = new_nums


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums_count = len(nums)
        k %= nums_count

        self.reverse(nums, 0, nums_count - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, nums_count - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
