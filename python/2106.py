from itertools import accumulate
from typing import List


# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/discuss/1624232/Python-Explanation-with-pictures-2-solutions.
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        right_boundary = max(startPos, fruits[-1][0])
        amount = [0] * (right_boundary + 1)
        for pos, count in fruits:
            amount[pos] = count

        prefix_sum = [0] + list(accumulate(amount))
        res = 0

        for right_dist in range(min(k, right_boundary - startPos) + 1):
            left_dist = max(0, k - 2 * right_dist)
            left_pos = max(0, startPos - left_dist)
            right_pos = startPos + right_dist
            res = max(res, prefix_sum[right_pos + 1] - prefix_sum[left_pos])

        for left_dist in range(min(k, startPos) + 1):
            right_dist = max(0, k - 2 * left_dist)
            right_pos = min(right_boundary, startPos + right_dist)
            left_pos = startPos - left_dist
            res = max(res, prefix_sum[right_pos + 1] - prefix_sum[left_pos])

        return res
