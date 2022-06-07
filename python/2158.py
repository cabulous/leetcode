from collections import defaultdict
from typing import List


# https://leetcode.com/problems/amount-of-new-area-painted-each-day/discuss/1958749/Python-beats-100
class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        seen = defaultdict()
        res = []

        for start, end in paint:
            work = 0

            while start < end:
                if start in seen:
                    start = seen[start]
                else:
                    seen[start] = end
                    work += 1
                    start += 1

            res.append(work)

        return res
