from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res, min_val, max_val = 0, float('inf'), float('-inf')

        for a in arrays:
            res = max(res, max(max_val - a[0], a[-1] - min_val))
            min_val = min(min_val, a[0])
            max_val = max(max_val, a[-1])

        return res
