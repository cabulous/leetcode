from typing import List


# https://leetcode.com/problems/range-sum-query-2d-immutable/discuss/75448/Sharing-My-Python-solution
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if matrix is None or not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        self.sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.sum[i][j] = matrix[i - 1][j - 1] + self.sum[i - 1][j] + self.sum[i][j - 1] - self.sum[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1 = row1 + 1, col1 + 1
        row2, col2 = row2 + 1, col2 + 1
        return self.sum[row2][col2] - self.sum[row2][col1 - 1] - self.sum[row1 - 1][col2] + self.sum[row1 - 1][col1 - 1]
