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
        seen = set(state)
        queue = [(self.dist_to_target(0, 0), 0, state)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while queue:
            min_dist, steps, (row, col, quota) = heapq.heappop(queue)
            if quota >= min_dist - steps:
                return min_dist
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    new_quota = quota - grid[nr][nc]
                    new_state = (nr, nc, new_quota)
                    if new_quota >= 0 and new_state not in seen:
                        seen.add(new_state)
                        new_min_dist = self.dist_to_target(nr, nc) + steps + 1
                        heapq.heappush(queue, (new_min_dist, steps + 1, new_state))

        return -1

    def dist_to_target(self, row, col):
        return (self.rows - row - 1) + (self.cols - col - 1)
