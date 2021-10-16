from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t1_cost, t2_cost = float('inf'), float('inf')
        t1_profit, t2_profit = 0, 0

        for price in prices:
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)
            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price - t2_cost)

        return t2_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        left_min = prices[0]
        right_max = prices[-1]

        length = len(prices)
        left_profits = [0] * length
        right_profits = [0] * (length + 1)

        for left in range(1, length):
            left_profits[left] = max(left_profits[left - 1], prices[left] - left_min)
            left_min = min(left_min, prices[left])

            right = length - left - 1
            right_profits[right] = max(right_profits[right + 1], right_max - prices[right])
            right_max = max(right_max, prices[right])

        max_profit = 0
        for i in range(length):
            max_profit = max(max_profit, left_profits[i] + right_profits[i + 1])

        return max_profit
