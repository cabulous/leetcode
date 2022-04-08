import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        queue = [-weight for weight in stones]
        heapq.heapify(queue)

        while len(queue) > 1:
            weight1 = -heapq.heappop(queue)
            weight2 = -heapq.heappop(queue)
            if weight1 != weight2:
                heapq.heappush(queue, -(weight1 - weight2))

        return -heapq.heappop(queue) if queue else 0
