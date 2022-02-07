import heapq
from typing import List


# https://leetcode.com/problems/the-skyline-problem/discuss/61261/10-line-Python-solution-104-ms/180903
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = [(left, -height, right) for left, right, height in buildings]
        events += list({(right, 0, 0) for _, right, _ in buildings})
        events.sort()

        res = [[0, 0]]
        live = [(0, float('inf'))]

        for pos, negative_height, right in events:
            while live[0][1] <= pos:
                heapq.heappop(live)
            if negative_height != 0:
                heapq.heappush(live, (negative_height, right))
            curr_height = -live[0][0]
            if res[-1][1] != curr_height:
                res += [[pos, curr_height]]

        return res[1:]
