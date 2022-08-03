import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        queue = []
        for r in range(min(rows, k)):
            heapq.heappush(queue, (matrix[r][0], r, 0))

        res = 0
        remain = k
        while remain > 0:
            res, r, c = heapq.heappop(queue)
            if c + 1 < cols:
                heapq.heappush(queue, (matrix[r][c + 1], r, c + 1))
            remain -= 1

        return res
