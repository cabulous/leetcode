import math
from typing import List


# https://leetcode.com/problems/maximum-number-of-visible-points/discuss/877822/Python-clean-sliding-window-solution-with-explanation
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        arr = []
        extra = 0
        xx, yy = location

        for x, y in points:
            if (x, y) == (xx, yy):
                extra += 1
                continue
            arr.append(math.atan2(y - yy, x - xx))

        arr.sort()
        arr = arr + [x + 2.0 * math.pi for x in arr]
        angle = math.pi * angle / 180

        left = 0
        res = 0
        for right in range(len(arr)):
            while arr[right] - arr[left] > angle:
                left += 1
            res = max(res, right - left + 1)

        return res + extra
