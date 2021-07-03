import bisect
from typing import List


# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/discuss/83596/Any-Accepted-Python-Solution/238097
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        assert len(matrix) > 0 and len(matrix[0]) > 0

        max_row = len(matrix)
        max_col = len(matrix[0])
        ans = float('-inf')

        for i in range(max_col):
            col_sum = [0] * max_row
            for j in range(i, max_col):
                cur_list = [0]
                row_sum = 0
                for r in range(max_row):
                    col_sum[r] += matrix[r][j]
                    row_sum += col_sum[r]
                    idx = bisect.bisect_left(cur_list, row_sum - k)
                    if 0 <= idx < len(cur_list):
                        ans = max(ans, row_sum - cur_list[idx])
                    if ans == k:
                        return ans
                    bisect.insort(cur_list, row_sum)

        return ans
