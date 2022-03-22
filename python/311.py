from typing import List


class SparseMatrix:

    def __init__(self, matrix, col_wise):
        self.values, self.row_index, self.col_index = self.compress_matrix(matrix, col_wise)

    def compress_matrix(self, matrix, col_wise):
        return self.compress_col_wise(matrix) if col_wise else self.compress_row_wise(matrix)

    def compress_row_wise(self, matrix):
        values = []
        row_index = [0]
        col_index = []

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col]:
                    values.append(matrix[row][col])
                    col_index.append(col)
            row_index.append(len(values))

        return values, row_index, col_index

    def compress_col_wise(self, matrix):
        values = []
        row_index = []
        col_index = [0]

        for col in range(len(matrix[0])):
            for row in range(len(matrix)):
                if matrix[row][col]:
                    values.append(matrix[row][col])
                    row_index.append(row)
            col_index.append(len(values))

        return values, row_index, col_index


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        matrix1 = SparseMatrix(mat1, False)
        matrix2 = SparseMatrix(mat2, True)

        res = [[0] * len(mat2[0]) for _ in range(len(mat1))]

        for row in range(len(res)):
            for col in range(len(res[0])):
                mat1_row_start = matrix1.row_index[row]
                mat1_row_end = matrix1.row_index[row + 1]

                mat2_col_start = matrix2.col_index[col]
                mat2_col_end = matrix2.col_index[col + 1]

                while mat1_row_start < mat1_row_end and mat2_col_start < mat2_col_end:
                    if matrix1.col_index[mat1_row_start] < matrix2.row_index[mat2_col_start]:
                        mat1_row_start += 1
                    elif matrix1.col_index[mat1_row_start] > matrix2.row_index[mat2_col_start]:
                        mat2_col_start += 1
                    else:
                        res[row][col] += matrix1.values[mat1_row_start] * matrix2.values[mat2_col_start]
                        mat1_row_start += 1
                        mat2_col_start += 1

        return res
