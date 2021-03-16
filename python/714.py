from typing import List


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash
