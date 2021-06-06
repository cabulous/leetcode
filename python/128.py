from typing import List


# hashset
# https://leetcode.com/problems/longest-consecutive-sequence/discuss/41057/Simple-O(n)-with-Explanation-Just-walk-each-streak
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 not in nums_set:
                next_num = num + 1
                while next_num in nums_set:
                    next_num += 1
                longest_streak = max(longest_streak, next_num - num)

        return longest_streak


# sorting
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        longest_streak = curr_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    curr_streak += 1
                else:
                    longest_streak = max(longest_streak, curr_streak)
                    curr_streak = 1

        return max(longest_streak, curr_streak)
