from typing import List


# https://leetcode.com/problems/longest-consecutive-sequence/discuss/41057/Simple-O(n)-with-Explanation-Just-walk-each-streak
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        res = 1

        for num in nums_set:
            if num - 1 not in nums_set:
                next_num = num + 1
                while next_num in nums_set:
                    next_num += 1
                res = max(res, next_num - num)

        return res
