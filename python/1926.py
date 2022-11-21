import heapq
from typing import List


class Solution:

    def __init__(self):
        self.entrance = []
        self.rows = 0
        self.cols = 0
        self.maze = []

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        self.entrance = entrance
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.maze = maze

        queue = [(0, entrance[0], entrance[1])]
        seen = {(entrance[0], entrance[1])}
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while queue:
            dist, row, col = heapq.heappop(queue)
            if self.is_exit(row, col):
                return dist
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols and self.can_walk(nr, nc) and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    heapq.heappush(queue, (dist + 1, nr, nc))

        return -1

    def is_exit(self, row, col):
        return [row, col] != self.entrance and (
                row in (0, self.rows - 1) or
                col in (0, self.cols - 1)
        )

    def can_walk(self, row, col):
        return self.maze[row][col] == '.'
