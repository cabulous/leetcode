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
