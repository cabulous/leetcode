from typing import List


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54131/Well-explained-Python-DP-with-comments
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        if k >= len(prices) // 2:
            return sum(
                sell - buy
                for sell, buy in zip(prices[1:], prices[:-1])
                if sell > buy
            )

        global_max = [[0] * len(prices) for _ in range(k + 1)]
        for i in range(1, k + 1):
            local_max = [0] * len(prices)
            for j in range(1, len(prices)):
                profit = prices[j] - prices[j - 1]
                local_max[j] = max(
                    local_max[j - 1] + profit,
                    global_max[i - 1][j - 1] + profit,
                    global_max[i - 1][j - 1],
                )
                global_max[i][j] = max(global_max[i][j - 1], local_max[j])

        return global_max[k][-1]
