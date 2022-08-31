from typing import List
from collections import deque


class Solution:

    def __init__(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.matrix = []
        self.rows = 0
        self.cols = 0

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        pacific_reachable = set()
        atlantic_reachable = set()

        for r in range(self.rows):
            self.dfs(r, 0, pacific_reachable)
            self.dfs(r, self.cols - 1, atlantic_reachable)

        for c in range(self.cols):
            self.dfs(0, c, pacific_reachable)
            self.dfs(self.rows - 1, c, atlantic_reachable)

        return list(pacific_reachable.intersection(atlantic_reachable))

    def dfs(self, row, col, reachable):
        reachable.add((row, col))

        for dr, dc in self.directions:
            nr, nc = row + dr, col + dc
            if nr < 0 or self.rows <= nr or nc < 0 or self.cols <= nc:
                continue
            if (nr, nc) in reachable:
                continue
            if self.matrix[nr][nc] < self.matrix[row][col]:
                continue
            self.dfs(nr, nc, reachable)


class Solution:

    def __init__(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.matrix = []
        self.rows = 0
        self.cols = 0

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        pacific_queue = deque()
        atlantic_queue = deque()

        for r in range(self.rows):
            pacific_queue.append((r, 0))
            atlantic_queue.append((r, self.cols - 1))

        for c in range(self.cols):
            pacific_queue.append((0, c))
            atlantic_queue.append((self.rows - 1, c))

        pacific_reachable = self.bfs(pacific_queue)
        atlantic_reachable = self.bfs(atlantic_queue)

        return list(pacific_reachable.intersection(atlantic_reachable))

    def bfs(self, queue):
        reachable = set()

        while queue:
            r, c = queue.popleft()
            reachable.add((r, c))

            for dr, dc in self.directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or self.rows <= nr or nc < 0 or self.cols <= nc:
                    continue
                if (nr, nc) in reachable:
                    continue
                if self.matrix[nr][nc] < self.matrix[r][c]:
                    continue
                queue.append((nr, nc))

        return reachable
