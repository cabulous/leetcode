class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1
        res = []

        while len(res) < rows * cols:
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            for row in range(top + 1, bottom + 1):
                res.append(matrix[row][right])
            if top != bottom:
                for col in reversed(range(left, right)):
                    res.append(matrix[bottom][col])
            if left != right:
                for row in reversed(range(top + 1, bottom)):
                    res.append(matrix[row][left])
            top += 1
            bottom -= 1
            left += 1
            right -= 1

        return res


# https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
