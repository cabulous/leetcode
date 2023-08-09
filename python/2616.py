# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/solutions/3883965/100-binary-search-greedy-video-in-o-n-log-m-optimal-solution/
class Solution:

    def __init__(self):
        self.nums = []
        self.goal = 0

    def minimizeMax(self, nums: list[int], p: int) -> int:
        self.nums = sorted(nums)
        self.goal = p

        left = 0
        right = self.nums[-1] - self.nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if self.can_pair(mid):
                right = mid
            else:
                left = mid + 1

        return left

    def can_pair(self, diff_max):
        count = 0
        i = 0
        while i < len(self.nums) - 1 and count < self.goal:
            if self.nums[i + 1] - self.nums[i] <= diff_max:
                count += 1
                i += 2
            else:
                i += 1
        return count >= self.goal
