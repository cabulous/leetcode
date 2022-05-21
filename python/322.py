import math


# https://leetcode.com/problems/coin-change/discuss/77372/Clean-dp-python-code
class Solution:
    def coinChange(self, coins, amount):
        dp = [0] + [math.inf] * amount

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[amount] if dp[amount] < math.inf else -1
