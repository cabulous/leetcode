class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        dp = [0] * (len(questions) + 1)

        for i in range(len(questions) - 1, -1, -1):
            points, skip = questions[i]
            dp[i] = max(
                points + dp[min(len(questions), i + 1 + skip)],
                dp[i + 1],
            )

        return dp[0]
