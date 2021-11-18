from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash_table = {}
        for num in nums:
            hash_table[num] = 1

        res = []
        for i in range(1, len(nums) + 1):
            if i not in hash_table:
                res.append(i)

        return res


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            new_index = abs(nums[i]) - 1
            if nums[new_index] > 0:
                nums[new_index] *= -1

        res = []
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                res.append(i)

        return res
