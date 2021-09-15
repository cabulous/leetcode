import math
from typing import List


# https://leetcode.com/problems/minimize-max-distance-to-gas-station/discuss/113633/C%2B%2BJavaPython-Binary-Search
class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        left, right = 1e-6, stations[-1] - stations[0]

        while left + 1e-6 < right:
            mid = left + (right - left) / 2
            count = 0
            for a, b in zip(stations, stations[1:]):
                count += math.ceil((b - a) / mid) - 1
            if count > k:
                left = mid
            else:
                right = mid

        return right
