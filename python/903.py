from itertools import accumulate

MOD = 10 ** 9 + 7


# https://leetcode.com/problems/valid-permutations-for-di-sequence/discuss/168278/C%2B%2BJavaPython-DP-Solution-O(N2)
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        dp = [1] * (len(s) + 1)
        for a, b in zip('I' + s, s):
            dp = list(accumulate(dp[:-1] if a == b else dp[-1:0:-1]))
        return dp[0] % MOD
