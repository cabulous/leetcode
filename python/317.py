import math
from typing import List
from collections import deque


# https://leetcode.com/problems/shortest-distance-from-all-buildings/discuss/76877/Python-solution-72ms-beats-100-BFS-with-pruning/80688
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        rows, cols = len(grid), len(grid[0])
        matrix = [[[0, 0] for _ in range(cols)] for _ in range(rows)]
        cnt = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    self.bfs(i, j, grid, matrix, cnt)
                    cnt += 1

        res = math.inf
        for i in range(rows):
            for j in range(cols):
                cur_step, cur_cnt = matrix[i][j]
                if cur_cnt == cnt:
                    res = min(res, cur_step)

        return res if res != math.inf else -1

    def bfs(self, row, col, grid, matrix, cnt):
        q = deque([(row, col, 0)])
        while q:
            r, c, step = q.popleft()
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                    continue
                if grid[nr][nc] != 0:
                    continue
                _, cur_cnt = matrix[nr][nc]
                if cur_cnt != cnt:
                    continue
                new_step, new_cnt = step + 1, cnt + 1
                matrix[nr][nc][0] += new_step
                matrix[nr][nc][1] = new_cnt
                q.append((nr, nc, new_step))
