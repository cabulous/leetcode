MOD = 10 ** 9 + 7


# https://leetcode.com/problems/profitable-schemes/solutions/154617/c-java-python-dp/?orderBy=most_votes
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        dp = [[0] * (n + 1) for _ in range(minProfit + 1)]
        dp[0][0] = 1

        for money, people in zip(profit, group):
            for i in range(minProfit, -1, -1):
                for j in range(n - people, -1, -1):
                    dp[min(minProfit, i + money)][j + people] += dp[i][j]

        return sum(dp[-1]) % MOD
