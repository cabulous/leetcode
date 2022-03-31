import heapq
from typing import List


class Solution:

    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.visited = []

    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        self.rows, self.cols = len(grid), len(grid[0])
        self.visited = [[False] * self.cols for _ in range(self.rows)]

        queue = [(-grid[0][0], 0, 0)]
        heapq.heapify(queue)
        self.visited[0][0] = True

        res = grid[0][0]

        while queue:
            _, row, col = heapq.heappop(queue)
            res = min(res, grid[row][col])

            if (row, col) == (self.rows - 1, self.cols - 1):
                return res

            for nr, nc in self.get_next_cell(row, col):
                heapq.heappush(queue, (-grid[nr][nc], nr, nc))

        return res

    def get_next_cell(self, row, col):
        for nr, nc in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if 0 <= nr < self.rows and 0 <= nc < self.cols and not self.visited[nr][nc]:
                self.visited[nr][nc] = True
                yield nr, nc
