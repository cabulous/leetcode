from typing import List

MOD = 10 ** 9 + 7


# https://leetcode.com/problems/sum-of-subsequence-widths/discuss/161267/JavaC%2B%2BPython-Sort-and-One-Pass
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        pow2 = [1]
        for i in range(1, n):
            pow2.append(pow2[-1] * 2 % MOD)

        res = 0
        for i, x in enumerate(nums):
            res = (res + (pow2[i] - pow2[n - 1 - i]) * x) % MOD

        return res
