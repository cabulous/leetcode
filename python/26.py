from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert = 1

        for scan in range(1, len(nums)):
            if nums[scan - 1] != nums[scan]:
                nums[insert] = nums[scan]
                insert += 1

        return insert
