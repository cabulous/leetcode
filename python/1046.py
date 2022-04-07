import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        queue = [-weight for weight in stones]
        heapq.heapify(queue)

        while len(queue) > 1:
            stone1 = heapq.heappop(queue)
            stone2 = heapq.heappop(queue)
            if stone1 != stone2:
                heapq.heappush(queue, stone1 - stone2)

        return -heapq.heappop(queue) if queue else 0
