import math


# https://leetcode.com/problems/coin-change/discuss/77372/Clean-dp-python-code
class Solution:
    def coinChange(self, coins, amount):
        dp = [0] + [math.inf] * amount

        for target in range(1, amount + 1):
            for coin in coins:
                if target - coin >= 0:
                    dp[target] = min(dp[target], 1 + dp[target - coin])

        return dp[amount] if dp[amount] < math.inf else -1
