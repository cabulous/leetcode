import copy
from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = set()
        queue = deque()
        res = copy.deepcopy(mat)

        for r in range(rows):
            for c in range(cols):
                if res[r][c] == 0:
                    visited.add((r, c))
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    res[nr][nc] = res[r][c] + 1
                    queue.append((nr, nc))

        return res
