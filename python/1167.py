from typing import List
import heapq


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        res = 0
        while len(sticks) > 1:
            stick1, stick2 = heapq.heappop(sticks), heapq.heappop(sticks)
            res += stick1 + stick2
            heapq.heappush(sticks, stick1 + stick2)
        return res
