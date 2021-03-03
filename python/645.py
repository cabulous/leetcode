from typing import List


# https://leetcode.com/problems/set-mismatch/discuss/105558/Oneliner-Python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        unique_sum = sum(set(nums))
        return [sum(nums) - unique_sum, sum(range(1, len(nums) + 1)) - unique_sum]
