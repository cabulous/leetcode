from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        max_row, max_col = len(mat), len(mat[0])
        visited = set()
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(max_row):
            for j in range(max_col):
                if mat[i][j] == 0:
                    visited.add((i, j))
                    queue.append((i, j))

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < max_row and 0 <= nc < max_col and (nr, nc) not in visited:
                    mat[nr][nc] = mat[r][c] + 1
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        return mat
