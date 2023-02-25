from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price_min = float('inf')
        res = 0

        for price in prices:
            price_min = min(price_min, price)
            res = max(res, price - price_min)

        return res
