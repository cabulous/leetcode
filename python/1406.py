# https://leetcode.com/problems/stone-game-iii/solutions/564260/java-c-python-dp-o-1-space/
class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        dp = [0] * 3

        for i in range(len(stoneValue) - 1, -1, -1):
            dp[i % 3] = max(
                sum(stoneValue[i:i + k]) - dp[(i + k) % 3]
                for k in (1, 2, 3)
            )

        if dp[0] == 0:
            return 'Tie'
        if dp[0] > 0:
            return 'Alice'
        return 'Bob'
