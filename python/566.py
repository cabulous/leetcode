from typing import List


# https://leetcode.com/problems/reshape-the-matrix/discuss/102499/Python-Simple-with-Explanation
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        values = iter(val for row in mat for val in row)
        return [[next(values) for _ in range(c)] for _ in range(r)]


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        assert len(mat) > 0 and len(mat[0]) > 0

        if len(mat) * len(mat[0]) != r * c:
            return mat

        new_mat = [[0] * c for _ in range(r)]
        next_val = self.get_next(mat)

        for i in range(r):
            for j in range(c):
                new_mat[i][j] = next(next_val)

        return new_mat

    def get_next(self, mat):
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                yield mat[i][j]
