from collections import Counter
from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        img1_ones = self.one_cells(img1)
        img2_ones = self.one_cells(img2)

        transformation_count = Counter()
        res = 0

        for x1, y1 in img1_ones:
            for x2, y2 in img2_ones:
                vec = (x2 - x1, y2 - y1)
                transformation_count[vec] += 1
                res = max(res, transformation_count[vec])

        return res

    def one_cells(self, matrix):
        res = []
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if val == 1:
                    res.append((r, c))
        return res
