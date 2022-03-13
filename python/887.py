# https://leetcode.com/problems/super-egg-drop/discuss/158974/C%2B%2BJavaPython-2D-and-1D-DP-O(KlogN)
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for move in range(1, n + 1):
            for egg in range(1, k + 1):
                dp[move][egg] = dp[move - 1][egg - 1] + dp[move - 1][egg] + 1
            if dp[move][k] >= n:
                return move


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [0, 0]
        move = 0
        while dp[-1] < n:
            for i in range(len(dp) - 1, 0, -1):
                dp[i] += dp[i - 1] + 1
            if len(dp) < k + 1:
                dp.append(dp[-1])
            move += 1
        return move
