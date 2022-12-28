from typing import List
import heapq


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-pile for pile in piles]
        heapq.heapify(max_heap)

        for _ in range(k):
            stone = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -(stone - stone // 2))

        return -sum(max_heap)
