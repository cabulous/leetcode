from typing import List
from collections import Counter


# https://leetcode.com/problems/largest-unique-number/discuss/344834/Python-3-One-liner
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        return max([k for k, v in Counter(A).items() if v == 1], default=-1)
