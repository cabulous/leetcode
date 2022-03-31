from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not any(matrix):
            return False

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            val = matrix[mid // cols][mid % cols]
            if val == target:
                return True
            if val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
