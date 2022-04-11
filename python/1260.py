from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        res = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                new_col = (col + k) % cols
                wrap_around = (col + k) // cols
                new_row = (row + wrap_around) % rows
                res[new_row][new_col] = grid[row][col]

        return res
