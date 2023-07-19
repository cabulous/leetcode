class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        __, range_end = intervals[0]
        res = 0

        for start, end in intervals[1:]:
            if start < range_end:
                res += 1
            else:
                range_end = end

        return res
