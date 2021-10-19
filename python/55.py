from typing import List


# https://leetcode.com/problems/jump-game/discuss/20907/1-6-lines-O(n)-time-O(1)-space
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        for i, n in enumerate(nums):
            if i > max_index:
                return False
            max_index = max(max_index, i + n)
        return True
