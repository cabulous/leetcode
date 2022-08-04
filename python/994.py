import copy
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        curr_grid = copy.deepcopy(grid)
        res = 0

        while queue:
            res += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and curr_grid[nr][nc] == 1:
                        fresh -= 1
                        curr_grid[nr][nc] = 2
                        queue.append((nr, nc))

        return max(0, res - 1) if fresh == 0 else -1
