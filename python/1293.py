import heapq
from typing import List
from collections import deque


class Solution:

    def __init__(self):
        self.rows = 0
        self.cols = 0

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])

        state = (0, 0, k)
        queue = [(self.dist_to_target(0, 0), 0, state)]
        seen = set(state)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while queue:
            estimation, steps, (row, col, quota) = heapq.heappop(queue)
            if quota >= estimation - steps:
                return estimation
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    new_quota = quota - grid[nr][nc]
                    new_state = (nr, nc, new_quota)
                    if new_quota >= 0 and new_state not in seen:
                        seen.add(new_state)
                        new_estimation = self.dist_to_target(nr, nc) + steps + 1
                        heapq.heappush(queue, (new_estimation, steps + 1, new_state))

        return -1

    def dist_to_target(self, row, col):
        return (self.rows - row - 1) + (self.cols - col - 1)


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        if k >= rows + cols - 2:
            return rows + cols - 2

        target = (rows - 1, cols - 1)
        state = (0, 0, k)
        queue = deque([(0, state)])
        seen = set(state)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while queue:
            steps, (row, col, quota) = queue.popleft()
            if (row, col) == target:
                return steps
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    n_quota = quota - grid[nr][nc]
                    n_state = (nr, nc, n_quota)
                    if n_quota >= 0 and n_state not in seen:
                        seen.add(n_state)
                        queue.append((steps + 1, n_state))

        return -1
