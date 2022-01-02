from collections import defaultdict
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = defaultdict(int)
        res = 0

        for t in time:
            if t % 60 == 0:
                res += remainders[0]
            else:
                res += remainders[60 - t % 60]
            remainders[t % 60] += 1

        return res
