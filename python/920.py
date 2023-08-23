import math

MOD = 10 ** 9 + 7


# https://leetcode.com/problems/number-of-music-playlists/discuss/178415/C%2B%2BJavaPython-DP-Solution
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        dp = [[0] * (goal + 1) for _ in range(n + 1)]

        for song_cnt in range(k + 1, n + 1):
            for goal_cnt in range(song_cnt, goal + 1):
                if song_cnt == goal_cnt:
                    dp[song_cnt][goal_cnt] = math.factorial(song_cnt)
                else:
                    dp[song_cnt][goal_cnt] = dp[song_cnt - 1][goal_cnt - 1] * song_cnt + dp[song_cnt][goal_cnt - 1] * (
                            song_cnt - k)

        return dp[-1][-1] % MOD
