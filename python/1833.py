from collections import Counter
from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        freq = Counter(costs)
        res = 0

        for cost in range(1, max(costs) + 1):
            if freq[cost] == 0:
                continue
            if coins < cost:
                return res
            count = min(freq[cost], coins // cost)
            coins -= cost * count
            res += count

        return res


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        res = 0
        for cost in sorted(costs):
            if coins - cost >= 0:
                coins -= cost
                res += 1
        return res
