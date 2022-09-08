from typing import List


# https://leetcode.com/problems/count-submatrices-with-all-ones/discuss/725108/Python-3-Dynamic-Programming
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])

        for r in range(rows):
            for c in range(1, cols):
                if mat[r][c] == 1:
                    mat[r][c] += mat[r][c - 1]

        res = 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] > 0:
                    width = mat[r][c]
                    curr_row = r
                    while curr_row < rows and mat[curr_row][c] > 0:
                        width = min(width, mat[curr_row][c])
                        res += width
                        curr_row += 1

        return res
