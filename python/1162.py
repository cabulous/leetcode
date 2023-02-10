from collections import deque


class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    queue.append((r, c, 0))
                    visited.add((r, c))

        if not queue or len(queue) == rows * cols:
            return -1

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        res = 0

        while queue:
            r, c, dist = queue.popleft()
            res = max(res, dist)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))

        return res
