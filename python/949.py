from itertools import permutations
from typing import List


# https://leetcode.com/problems/largest-time-for-given-digits/discuss/200517/Python-1-line-Check-Permutations-O(24)
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        for perm in permutations(sorted(arr, reverse=True)):
            if perm[0] * 10 + perm[1] < 24 and perm[2] < 6:
                return f"{perm[0]}{perm[1]}:{perm[2]}{perm[3]}"
        return ''
