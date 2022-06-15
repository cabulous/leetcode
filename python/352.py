import heapq
from typing import List


# https://leetcode.com/problems/data-stream-as-disjoint-intervals/discuss/82548/Share-my-python-solution-using-heap/1373330
class SummaryRanges:

    def __init__(self):
        self.intervals = []
        self.seen = set()

    def addNum(self, val: int) -> None:
        if val in self.seen:
            return
        self.seen.add(val)
        heapq.heappush(self.intervals, [val, val])

    def getIntervals(self) -> List[List[int]]:
        self.intervals = self.clean_intervals(self.intervals)
        return self.intervals

    def clean_intervals(self, intervals):
        res = []
        while intervals:
            curr = heapq.heappop(intervals)
            if res and curr[0] == res[-1][1] + 1:
                res[-1][1] = curr[1]
            else:
                res.append(curr)
        return res
