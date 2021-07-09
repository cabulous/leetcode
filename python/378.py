import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []

        for r in range(min(k, n)):
            heapq.heappush(heap, (matrix[r][0], r, 0))

        res = 0

        while k > 0:
            res, r, c = heapq.heappop(heap)
            if c < n - 1:
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))
            k -= 1

        return res
