import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-weight for weight in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            w1 = -heapq.heappop(max_heap)
            w2 = -heapq.heappop(max_heap)
            if w1 != w2:
                heapq.heappush(max_heap, -abs(w1 - w2))

        if not max_heap:
            return 0

        return -max_heap.pop()
