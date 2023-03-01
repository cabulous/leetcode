class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        return self.merge_sort(nums)

    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.merge_sort(nums[mid:])
        right = self.merge_sort(nums[:mid])

        return self.merge(left, right)

    def merge(self, left_nums, right_nums):
        left = 0
        right = 0
        res = []

        while left < len(left_nums) and right < len(right_nums):
            if left_nums[left] <= right_nums[right]:
                res.append(left_nums[left])
                left += 1
            else:
                res.append(right_nums[right])
                right += 1

        res += left_nums[left:]
        res += right_nums[right:]

        return res
