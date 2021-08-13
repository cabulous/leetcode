from typing import List
from itertools import product


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        max_row, max_col = len(matrix), len(matrix[0])
        rows, cols = set(), set()

        for i, j in product(range(max_row), range(max_col)):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

        for i, j in product(range(max_row), range(max_col)):
            if i in rows or j in cols:
                matrix[i][j] = 0


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        max_row, max_col = len(matrix), len(matrix[0])
        is_col = False

        for i in range(max_row):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, max_col):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, max_row):
            for j in range(1, max_col):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(max_col):
                matrix[0][j] = 0

        if is_col:
            for i in range(max_row):
                matrix[i][0] = 0
