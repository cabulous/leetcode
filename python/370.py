from typing import List
from itertools import accumulate


# https://leetcode.com/problems/range-addition/discuss/84220/O(n%2Bk)-Python-Solution
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * length
        for start, end, inc in updates:
            res[start] += inc
            if end + 1 <= length - 1:
                res[end + 1] -= inc

        return list(accumulate(res))
