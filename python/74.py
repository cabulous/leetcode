class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols

        while left < right:
            mid = left + (right - left) // 2
            val = matrix[mid // cols][mid % cols]
            if val == target:
                return True
            if val < target:
                left = mid + 1
            else:
                right = mid

        return False
