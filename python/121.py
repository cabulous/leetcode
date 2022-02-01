from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price_min = float('inf')
        res = 0

        for price in prices:
            if price < price_min:
                price_min = price
            elif price - price_min > res:
                res = price - price_min

        return res
