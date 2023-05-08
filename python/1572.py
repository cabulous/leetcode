class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        res = 0

        for i in range(len(mat)):
            res += mat[i][i]
            res += mat[len(mat) - 1 - i][i]

        if len(mat) % 2 == 1:
            mid = len(mat) // 2
            res -= mat[mid][mid]

        return res
