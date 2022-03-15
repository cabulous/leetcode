import heapq
from typing import List


# https://leetcode.com/problems/trapping-rain-water-ii/discuss/89466/python-solution-with-heap
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        rows, cols = len(heightMap), len(heightMap[0])
        visited = [[False] * cols for _ in range(rows)]
        queue = []

        for r in range(rows):
            for c in range(cols):
                if r in (0, rows - 1) or c in (0, cols - 1):
                    visited[r][c] = True
                    heapq.heappush(queue, (heightMap[r][c], r, c))

        res = 0
        while queue:
            height, r, c = heapq.heappop(queue)
            res += max(height - heightMap[r][c], 0)
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(queue, (max(height, heightMap[nr][nc]), nr, nc))

        return res
