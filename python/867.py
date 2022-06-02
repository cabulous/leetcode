from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        res = [[0] * rows for _ in range(cols)]

        for row in range(rows):
            for col in range(cols):
                res[col][row] = matrix[row][col]

        return res
