import math

MOD = 10 ** 9 + 7


# https://leetcode.com/problems/number-of-music-playlists/discuss/178415/C%2B%2BJavaPython-DP-Solution
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        dp = [[0] * (goal + 1) for _ in range(n + 1)]

        for i in range(k + 1, n + 1):
            for j in range(i, goal + 1):
                if i == j:
                    dp[i][j] = math.factorial(i)
                else:
                    dp[i][j] = dp[i - 1][j - 1] * i + dp[i][j - 1] * (i - k)

        return dp[-1][-1] % MOD
