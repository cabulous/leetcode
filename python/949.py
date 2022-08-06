from itertools import permutations
from typing import List


# https://leetcode.com/problems/largest-time-for-given-digits/discuss/200517/Python-1-line-Check-Permutations-O(24)
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        for perm in permutations(sorted(arr, reverse=True)):
            d1, d2, d3, d4 = perm
            if d1 * 10 + d2 < 24 and d3 < 6:
                return f'{d1}{d2}:{d3}{d4}'
        return ''
