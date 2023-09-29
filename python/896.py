class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        increase = False
        decrease = False

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                increase = True
            if nums[i - 1] > nums[i]:
                decrease = True

        return not (increase and decrease)
