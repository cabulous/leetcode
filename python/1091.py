from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row, max_col = len(grid), len(grid[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        if grid[0][0] == 1 or grid[max_row - 1][max_col - 1] == 1:
            return -1

        queue = deque([(0, 0, 1)])
        visited = {(0, 0)}

        while queue:
            row, col, distance = queue.popleft()
            if row == max_row - 1 and col == max_col - 1:
                return distance
            for dx, dy in directions:
                nr, nc = row + dx, col + dy
                if 0 <= nr < max_row and 0 <= nc < max_col and (nr, nc) not in visited and grid[nr][nc] == 0:
                    visited.add((nr, nc))
                    queue.append((nr, nc, distance + 1))

        return -1
