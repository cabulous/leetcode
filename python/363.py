import bisect
import math
from typing import List


# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/discuss/83596/Any-Accepted-Python-Solution/238097
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        res = -math.inf

        for c1 in range(cols):
            col_sum = [0] * rows
            for c2 in range(c1, cols):
                cur_list = [0]
                row_sum = 0
                for r in range(rows):
                    col_sum[r] += matrix[r][c2]
                    row_sum += col_sum[r]
                    idx = bisect.bisect_left(cur_list, row_sum - k)
                    if 0 <= idx < len(cur_list):
                        res = max(res, row_sum - cur_list[idx])
                    if res == k:
                        return k
                    bisect.insort(cur_list, row_sum)

        return res
