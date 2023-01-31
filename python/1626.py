# https://leetcode.com/problems/best-team-with-no-conflicts/solutions/3120787/day-31-c-dp-easiest-beginner-friendly-sol-o-n-2-time-and-o-n-space/
class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        player = sorted(zip(ages, scores))
        dp = [0] * len(player)
        res = 0

        for i in range(len(player)):
            __, curr_score = player[i]
            dp[i] = curr_score
            for j in range(i):
                __, prev_score = player[j]
                if prev_score <= curr_score:
                    dp[i] = max(dp[i], dp[j] + curr_score)
            res = max(res, dp[i])

        return res
