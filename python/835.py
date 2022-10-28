from collections import Counter
from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        img1_ones = self.non_zero_cells(img1)
        img2_ones = self.non_zero_cells(img2)

        transformation_count = Counter()
        res = 0

        for x_img1, y_img1 in img1_ones:
            for x_img2, y_img2 in img2_ones:
                vec = (x_img2 - x_img1, y_img2 - y_img1)
                transformation_count[vec] += 1
                res = max(res, transformation_count[vec])

        return res

    def non_zero_cells(self, matrix):
        res = []
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 1:
                    res.append((r, c))
        return res
