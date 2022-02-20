from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        prev_end = 0
        res = 0

        for _, end in intervals:
            if prev_end < end:
                res += 1
                prev_end = end

        return res
