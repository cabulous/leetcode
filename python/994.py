from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not any(grid):
            return -1

        rows, cols = len(grid), len(grid[0])
        fresh_orange = 0
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_orange += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        queue.append((-1, -1))
        time_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while queue:
            r, c = queue.popleft()
            if r == -1:
                time_elapsed += 1
                if queue:
                    queue.append((-1, -1))
            else:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    if grid[nr][nc] == 0:
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_orange -= 1
                        queue.append((nr, nc))

        return time_elapsed if fresh_orange == 0 else -1
