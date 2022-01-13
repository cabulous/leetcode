from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        prev_end = points[0][1]
        arrow_count = 1

        for start, end in points[1:]:
            if prev_end < start:
                arrow_count += 1
                prev_end = end

        return arrow_count
