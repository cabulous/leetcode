from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(numRows):
            row = [1] * (row_num + 1)
            for col in range(1, len(row) - 1):
                row[col] = triangle[row_num - 1][col - 1] + triangle[row_num - 1][col]
            triangle.append(row)

        return triangle
