import bisect
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        res = []

        for start, end in intervals:
            if end < new_start:
                res.append([start, end])
            elif new_end < start:
                res.append([new_start, new_end])
                new_start = start
                new_end = end
            else:
                new_start = min(new_start, start)
                new_end = max(new_end, end)

        res.append([new_start, new_end])

        return res


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = bisect.bisect_left(intervals, newInterval)
        intervals.insert(idx, newInterval)

        i = 0
        while i < len(intervals):
            start, end = intervals[i]
            prev_start, prev_end = intervals[i - 1]
            if i > 0 and start <= prev_end:
                intervals[i - 1:i + 1] = [[prev_start, max(prev_end, end)]]
            else:
                i += 1

        return intervals
