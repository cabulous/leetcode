from collections import Counter
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = Counter()
        count[0] = 1

        prefix_sum = 0
        res = 0

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            res += count[remainder]
            count[remainder] += 1

        return res
