from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        max_row, max_col = len(matrix), len(matrix[0])
        r, c = max_row - 1, 0

        while r >= 0 and c < max_col:
            if matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target:
                c += 1
            else:
                return True

        return False
