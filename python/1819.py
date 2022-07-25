from math import gcd
from typing import List


# https://leetcode.com/problems/number-of-different-subsequences-gcds/discuss/1141361/Python-Python-2-solutions-%2B-2liner-explained
class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        max_num = max(nums)
        nums_set = set(nums)
        res = 0

        for cand in range(1, max_num + 1):
            curr_gcd = 0
            for num in range(cand, max_num + 1, cand):
                if num in nums_set:
                    curr_gcd = gcd(curr_gcd, num)
                if curr_gcd == cand:
                    res += 1
                    break

        return res
