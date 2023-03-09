import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2
            hour_needed = sum(math.ceil(p / mid) for p in piles)
            if hour_needed <= h:
                right = mid
            else:
                left = mid + 1

        return left
