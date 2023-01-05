from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key=lambda x: x[1])

        prev_end = sorted_points[0][1]
        res = 1

        for start, end in sorted_points[1:]:
            if prev_end < start:
                prev_end = end
                res += 1

        return res
