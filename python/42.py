from typing import List


# https://leetcode.com/problems/trapping-rain-water/discuss/17554/Share-my-one-pass-Python-solution-with-explaination
# two pointers
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        left = 0
        right = len(height) - 1
        left_height_max = height[0]
        right_height_max = height[-1]
        res = 0

        while left < right:
            left_height_max = max(left_height_max, height[left])
            right_height_max = max(right_height_max, height[right])
            if left_height_max <= right_height_max:
                res += left_height_max - height[left]
                left += 1
            else:
                res += right_height_max - height[right]
                right -= 1

        return res


# dp
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        left_height_max = [0] * len(height)
        left_height_max[0] = height[0]
        for i in range(1, len(height)):
            left_height_max[i] = max(left_height_max[i - 1], height[i])

        right_height_max = [0] * len(height)
        right_height_max[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right_height_max[i] = max(right_height_max[i + 1], height[i])

        res = 0
        for i in range(1, len(height)):
            res += min(left_height_max[i], right_height_max[i]) - height[i]

        return res
