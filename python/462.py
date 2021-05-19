from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = sorted(nums)[len(nums) // 2]
        return sum(abs(num - median) for num in nums)


# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/discuss/94923/2-lines-Python-2-ways
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[~i] - nums[i] for i in range(len(nums) // 2))
