import math
from typing import List


# https://leetcode.com/problems/maximum-number-of-visible-points/discuss/877822/Python-clean-sliding-window-solution-with-explanation
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        angle_group = []
        extra = 0
        xx, yy = location

        for x, y in points:
            if (x, y) == (xx, yy):
                extra += 1
                continue
            angle_group.append(math.atan2(y - yy, x - xx))

        angle_group.sort()
        angle_group = angle_group + [x + 2.0 * math.pi for x in angle_group]
        angle_max = math.pi * angle / 180

        left = 0
        res = 0
        for right in range(len(angle_group)):
            while angle_group[right] - angle_group[left] > angle_max:
                left += 1
            res = max(res, right - left + 1)

        return res + extra
