import math
from itertools import accumulate


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        prefix_sum = [0]

        for digit in s:
            prefix_sum.append(prefix_sum[-1] + int(digit))

        res = math.inf

        for i in range(len(prefix_sum)):
            cur = prefix_sum[i] + (len(s) - i - (prefix_sum[-1] - prefix_sum[i]))
            res = min(res, cur)

        return res
