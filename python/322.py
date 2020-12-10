# DP
# https://leetcode.com/problems/coin-change/discuss/77372/Clean-dp-python-code
class Solution:
    def coinChange(self, coins, amount):
        dp = [0.0] + [float('inf')] * amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return int(dp[-1]) if dp[-1] != float('inf') else -1
