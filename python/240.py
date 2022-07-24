from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not any(matrix):
            return False

        rows = len(matrix)
        cols = len(matrix[0])
        r = rows - 1
        c = 0

        while r >= 0 and c < cols:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target:
                c += 1

        return False
