from collections import deque


# https://leetcode.com/problems/sliding-window-maximum/solutions/65901/9-lines-ruby-11-lines-python-o-n/
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        queue = deque()
        res = []

        for i, num in enumerate(nums):
            while queue and nums[queue[-1]] < num:
                queue.pop()
            queue.append(i)
            if queue[0] == i - k:
                queue.popleft()
            if i >= k - 1:
                res.append(nums[queue[0]])

        return res
