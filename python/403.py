# https://leetcode.com/problems/frog-jump/discuss/88800/Python-Documented-solution-that-is-easy-to-understand/93592
class Solution:
    def canCross(self, stones: list[int]) -> bool:
        if stones[1] != 1:
            return False

        dp = {stone: set() for stone in stones}
        dp[1].add(1)

        for stone in stones[:-1]:
            for prev_jump in dp[stone]:
                for jump in range(prev_jump - 1, prev_jump + 2):
                    if jump > 0 and stone + jump in dp:
                        dp[stone + jump].add(jump)

        return len(dp[stones[-1]]) > 0
