from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        row, col = 0, 0
        dr, dc = 0, 1

        for num in range(1, n * n + 1):
            res[row][col] = num

            next_row = (row + dr) % n
            next_col = (col + dc) % n
            if res[next_row][next_col] != 0:
                dr, dc = dc, -dr

            row += dr
            col += dc

        return res
