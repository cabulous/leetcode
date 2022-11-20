import heapq
from typing import List


class Solution:

    def __init__(self):
        self.rows = 0
        self.cols = 0

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])

        state = (0, 0, k)
        seen = {state}
        queue = [(self.dist_to_target(0, 0), 0, state)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while queue:
            min_dist, steps, (row, col, quota) = heapq.heappop(queue)
            if quota >= min_dist - steps:
                return min_dist
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    next_quota = quota - grid[nr][nc]
                    next_state = (nr, nc, next_quota)
                    if next_quota >= 0 and next_state not in seen:
                        seen.add(next_state)
                        next_min_dist = self.dist_to_target(nr, nc) + steps + 1
                        heapq.heappush(queue, (next_min_dist, steps + 1, next_state))

        return -1

    def dist_to_target(self, row, col):
        return (self.rows - row - 1) + (self.cols - col - 1)
