from math import gcd
from typing import List


# https://leetcode.com/problems/number-of-different-subsequences-gcds/discuss/1141361/Python-Python-2-solutions-%2B-2liner-explained
class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        max_num = max(nums)
        nums_set = set(nums)
        res = 0

        for x in range(1, max_num + 1):
            curr = 0
            for y in range(x, max_num + 1, x):
                if y in nums_set:
                    curr = gcd(curr, y)
                if curr == x:
                    res += 1
                    break

        return res
