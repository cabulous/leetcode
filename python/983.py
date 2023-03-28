class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        dp = [0] * (days[-1] + 1)

        for i in range(len(dp)):
            if i in days:
                dp[i] = min(
                    dp[max(0, i - 1)] + costs[0],
                    dp[max(0, i - 7)] + costs[1],
                    dp[max(0, i - 30)] + costs[2],
                )
            else:
                dp[i] = dp[i - 1]

        return dp[-1]
