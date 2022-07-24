from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not any(matrix):
            return False

        rows = len(matrix)
        cols = len(matrix[0])
        r = rows - 1
        c = 0

        while 0 <= r and c < cols:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] < target:
                c += 1
            else:
                r -= 1

        return False
