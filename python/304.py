from typing import List


# https://leetcode.com/problems/range-sum-query-2d-immutable/discuss/75448/Sharing-My-Python-solution
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not any(matrix):
            return

        rows = len(matrix)
        cols = len(matrix[0])
        self.sum = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                self.sum[r][c] = matrix[r][c] + self.sum[r - 1][c] + self.sum[r][c - 1] - self.sum[r - 1][c - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum[row2][col2] - self.sum[row1 - 1][col2] - self.sum[row2][col1 - 1] + self.sum[row1 - 1][col1 - 1]
