from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = float('-inf')
        held = float('-inf')
        reset = 0

        for price in prices:
            sold, held, reset = held + price, max(held, reset - price), max(reset, sold)

        return max(sold, reset)
