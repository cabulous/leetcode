from itertools import accumulate
from typing import List


# https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/discuss/987347/JavaC%2B%2BPython-Solution
class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        indexes = [i for i, num in enumerate(nums) if num == 1]
        prefix_sum = [0] + list(accumulate(indexes))
        res = float('inf')

        for i in range(len(indexes) - k + 1):
            res = min(
                res,
                prefix_sum[i + k] - prefix_sum[k // 2 + i] - prefix_sum[(k + 1) // 2 + i] + prefix_sum[i]
            )

        res -= (k // 2) * ((k + 1) // 2)

        return res
