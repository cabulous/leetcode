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
        ptr1 = 1

        for ptr2 in range(1, len(nums)):
            if nums[ptr2 - 1] == nums[ptr2]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[ptr1] = nums[ptr2]
                ptr1 += 1

        return ptr1
