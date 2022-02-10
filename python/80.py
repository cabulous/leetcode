from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        index = 1

        while index < len(nums):
            if nums[index - 1] == nums[index]:
                count += 1
                if count > 2:
                    nums.pop(index)
                    index -= 1
            else:
                count = 1
            index += 1

        return len(nums)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        slow = 1

        for fast in range(1, len(nums)):

            if nums[fast - 1] == nums[fast]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[slow] = nums[fast]
                slow += 1

        return slow
