from typing import List


# https://leetcode.com/problems/jump-game/discuss/20907/1-6-lines-O(n)-time-O(1)-space
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_idx = 0

        for i, dist in enumerate(nums):
            if max_idx < i:
                return False
            max_idx = max(max_idx, i + dist)

        return True
