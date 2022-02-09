from collections import Counter
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        res = 0

        for num in count:
            if k > 0 and num + k in count:
                res += 1
            elif k == 0 and count[num] > 1:
                res += 1

        return res
