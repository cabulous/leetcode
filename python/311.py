class SparseMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.values, self.row_index, self.col_index = self.compress(matrix)

    def compress(self, matrix: list[list[int]]) -> tuple[list[int], list[int], list[int]]:
        raise NotImplementedError('Implement it in the subclass')


class RowWiseSparseMatrix(SparseMatrix):
    def compress(self, matrix: list[list[int]]) -> tuple[list[int], list[int], list[int]]:
        values = []
        row_idx = [0]
        col_idx = []

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] != 0:
                    values.append(matrix[r][c])
                    col_idx.append(c)
            row_idx.append(len(values))

        return values, row_idx, col_idx


class ColWiseSparseMatrix(SparseMatrix):
    def compress(self, matrix: list[list[int]]) -> tuple[list[int], list[int], list[int]]:
        values = []
        row_idx = []
        col_idx = [0]

        for c in range(len(matrix[0])):
            for r in range(len(matrix)):
                if matrix[r][c] != 0:
                    values.append(matrix[r][c])
                    row_idx.append(r)
            col_idx.append(len(values))

        return values, row_idx, col_idx


class Solution:
    def multiply(self, mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
        matrix1 = RowWiseSparseMatrix(mat1)
        matrix2 = ColWiseSparseMatrix(mat2)
        res = [[0] * len(mat2[0]) for _ in range(len(mat1))]

        for r in range(len(res)):
            for c in range(len(res[0])):
                mat1_row_start = matrix1.row_index[r]
                mat1_row_end = matrix1.row_index[r + 1]

                mat2_col_start = matrix2.col_index[c]
                mat2_col_end = matrix2.col_index[c + 1]

                while mat1_row_start < mat1_row_end and mat2_col_start < mat2_col_end:
                    if matrix1.col_index[mat1_row_start] < matrix2.row_index[mat2_col_start]:
                        mat1_row_start += 1
                    elif matrix1.col_index[mat1_row_start] > matrix2.row_index[mat2_col_start]:
                        mat2_col_start += 1
                    else:
                        res[r][c] += matrix1.values[mat1_row_start] * matrix2.values[mat2_col_start]
                        mat1_row_start += 1
                        mat2_col_start += 1

        return res
