from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        row_max, col_max = len(matrix), len(matrix[0])
        r, c = row_max - 1, 0

        while c < col_max and r >= 0:
            if matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target:
                c += 1
            else:
                return True

        return False
