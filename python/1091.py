from typing import List
from collections import deque


class Solution:

    def __init__(self):
        self.grid = []
        self.rows = 0
        self.cols = 0
        self.directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        self.visited = set()

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        queue = deque([(0, 0, 1)])
        target = (self.rows - 1, self.cols - 1)

        while queue:
            row, col, dist = queue.popleft()
            if (row, col) == target:
                return dist
            for next_row, next_col in self.get_next_step(row, col):
                queue.append((next_row, next_col, dist + 1))

        return -1

    def get_next_step(self, row, col):
        for dr, dc in self.directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and (nr, nc) not in self.visited and self.grid[nr][nc] == 0:
                self.visited.add((nr, nc))
                yield nr, nc
