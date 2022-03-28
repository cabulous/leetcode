import bisect
from itertools import combinations

from typing import List


# https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/discuss/1513368/C%2B%2BPython3-binary-search
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        left, right = nums[:n], nums[n:]
        left_sum, right_sum = sum(left), sum(right)

        res = float('inf')

        for i in range(n + 1):
            vals = sorted(2 * sum(combo) - left_sum for combo in combinations(left, i))
            for combo in combinations(right, n - i):
                diff = 2 * sum(combo) - right_sum
                k = bisect.bisect_left(vals, -diff)
                if k > 0:
                    res = min(res, abs(vals[k - 1] + diff))
                if k < len(vals):
                    res = min(res, abs(vals[k] + diff))

        return res
