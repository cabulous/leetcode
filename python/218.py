import heapq
import math
from typing import List


# https://leetcode.com/problems/the-skyline-problem/discuss/61261/10-line-Python-solution-104-ms/180903
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = [(left, -height, right) for left, right, height in buildings]
        events.extend([(right, 0, 0) for _, right, _ in buildings])
        events.sort()

        res = [[0, 0]]
        live = [(0, math.inf)]
        for start, neg_height, end in events:
            while live[0][1] <= start:
                heapq.heappop(live)
            if neg_height != 0:
                heapq.heappush(live, (neg_height, end))
            curr_height = -live[0][0]
            if curr_height != res[-1][1]:
                res.append([start, curr_height])

        return res[1:]
