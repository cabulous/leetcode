from functools import lru_cache
from typing import List


class Solution:

    def __init__(self):
        self.matrix = []
        self.rows = 0
        self.cols = 0

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        res = float('inf')
        for col in range(self.cols):
            res = min(res, self.helper(0, col))

        return int(res)

    @lru_cache(None)
    def helper(self, row, col):
        if col < 0 or self.cols <= col:
            return float('inf')

        if row == self.rows - 1:
            return self.matrix[row][col]

        left = self.helper(row + 1, col - 1)
        mid = self.helper(row + 1, col)
        right = self.helper(row + 1, col + 1)

        return self.matrix[row][col] + min(left, mid, right)
