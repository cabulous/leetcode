from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remaining = [cap - rock for cap, rock in zip(capacity, rocks)]
        remaining.sort()

        res = 0
        for curr in remaining:
            if additionalRocks < curr:
                return res
            additionalRocks -= curr
            res += 1

        return res
