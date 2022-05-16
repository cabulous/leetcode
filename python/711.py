import copy
from typing import List


# https://leetcode.com/problems/number-of-distinct-islands-ii/discuss/137652/Python-DFS-solution
class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    shape = []
                    self.dfs(grid, r, c, shape)
                    norm = self.normalize(shape)
                    res.add(norm)

        return len(res)

    def dfs(self, grid, r, c, shape):
        grid[r][c] = 0
        shape.append((r, c))

        rows, cols = len(grid), len(grid[0])
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 0:
                self.dfs(grid, nr, nc, shape)

    def normalize(self, shape):
        rotated_shapes = [[] for _ in range(8)]

        for x, y in shape:
            rotated_shapes[0].append((x, y))
            rotated_shapes[1].append((-x, y))
            rotated_shapes[2].append((x, -y))
            rotated_shapes[3].append((-x, -y))
            rotated_shapes[4].append((y, x))
            rotated_shapes[5].append((-y, x))
            rotated_shapes[6].append((y, -x))
            rotated_shapes[7].append((-y, -x))

        for rotated in rotated_shapes:
            rotated.sort()

        res = []
        for rotated in rotated_shapes:
            tmp = [(0, 0)]
            for i in range(1, len(rotated)):
                x1, y1 = rotated[0]
                x2, y2 = rotated[i]
                tmp.append((x2 - x1, y2 - y1))
            res.append(tmp[:])

        res.sort()

        return tuple(res[0])
