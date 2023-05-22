LAND = 1
WATER = 0


class Solution:

    def __init__(self):
        self.grid = []
        self.rows = 0
        self.cols = 0
        self.queue = []
        self.visited = set()
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def shortestBridge(self, grid: list[list[int]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        start_row, start_col = self.first_land()
        self.dfs(start_row, start_col)

        queue = self.queue
        step = 0
        while queue:
            next_queue = []
            for row, col in queue:
                for dr, dc in self.directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols and (nr, nc) not in self.visited:
                        if grid[nr][nc] == LAND:
                            return step
                        self.visited.add((nr, nc))
                        next_queue.append((nr, nc))
            step += 1
            queue = next_queue

        return -1

    def dfs(self, row, col):
        self.visited.add((row, col))
        self.queue.append((row, col))
        for dr, dc in self.directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and (nr, nc) not in self.visited and self.grid[nr][nc] == LAND:
                self.dfs(nr, nc)

    def first_land(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == LAND:
                    return r, c
