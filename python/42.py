from typing import List


# https://leetcode.com/problems/trapping-rain-water/discuss/17554/Share-my-one-pass-Python-solution-with-explaination
# two pointers
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[0], height[-1]
        res = 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max <= right_max:
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1

        return res


# dp
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        if not height or n < 3:
            return 0

        left_max = [0] * n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max = [0] * n
        right_max[-1] = height[-1]
        for i in reversed(range(1, n)):
            right_max[i - 1] = max(right_max[i], height[i - 1])

        res = 0
        for i in range(1, n):
            res += min(left_max[i], right_max[i]) - height[i]

        return res
