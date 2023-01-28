import heapq
from typing import List


# https://leetcode.com/problems/data-stream-as-disjoint-intervals/discuss/82548/Share-my-python-solution-using-heap/1373330
class SummaryRanges:

    def __init__(self):
        self.intervals = []
        self.seen = set()

    def addNum(self, value: int) -> None:
        if value in self.seen:
            return
        self.seen.add(value)
        heapq.heappush(self.intervals, [value, value])

    def _clean_up(self):
        res = []
        while self.intervals:
            curr = heapq.heappop(self.intervals)
            if res and res[-1][1] + 1 == curr[0]:
                res[-1][1] = curr[1]
            else:
                res.append(curr)
        self.intervals = res

    def getIntervals(self) -> List[List[int]]:
        self._clean_up()
        return self.intervals
