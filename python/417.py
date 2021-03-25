from typing import List
from collections import deque


# dfs
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        max_row, max_col = len(matrix), len(matrix[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(row, col, reachable):
            reachable.add((row, col))
            for dx, dy in directions:
                nr, nc = row + dx, col + dy
                if nr < 0 or nr >= max_row or nc < 0 or nc >= max_col:
                    continue
                if (nr, nc) in reachable:
                    continue
                if matrix[nr][nc] < matrix[row][col]:
                    continue
                dfs(nr, nc, reachable)

        for i in range(max_row):
            dfs(i, 0, pacific_reachable)
            dfs(i, max_col - 1, atlantic_reachable)
        for i in range(max_col):
            dfs(0, i, pacific_reachable)
            dfs(max_row - 1, i, atlantic_reachable)

        return list(pacific_reachable.intersection(atlantic_reachable))


# bfs
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        max_row, max_col = len(matrix), len(matrix[0])
        pacific_queue = deque()
        atlantic_queue = deque()

        for i in range(max_row):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, max_col - 1))
        for i in range(max_col):
            pacific_queue.append((0, i))
            atlantic_queue.append((max_row - 1, i))

        def bfs(queue):
            reachable = set()
            while queue:
                row, col = queue.popleft()
                reachable.add((row, col))
                for dx, dy in directions:
                    nr, nc = row + dx, col + dy
                    if nr < 0 or nr >= max_row or nc < 0 or nc >= max_col:
                        continue
                    if (nr, nc) in reachable:
                        continue
                    if matrix[nr][nc] < matrix[row][col]:
                        continue
                    queue.append((nr, nc))
            return reachable

        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)

        return list(pacific_reachable.intersection(atlantic_reachable))
