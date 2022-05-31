from functools import lru_cache

MOD = 10 ** 9 + 7


# https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/discuss/1163050/Python-O(26n)-math-solution-explained
class Solution:
    def makeStringSorted(self, s: str) -> int:
        n = len(s)
        count = [0] * 26
        res = 0

        for i in range(n - 1, -1, -1):
            ind = ord(s[i]) - ord('a')
            count[ind] += 1
            curr = sum(count[:ind]) * self.f(n - i - 1)
            for j in range(26):
                curr *= self.inv(self.f(count[j])) % MOD
            res += curr

        return res % MOD

    @lru_cache(None)
    def f(self, i):
        return 1 if i <= 1 else self.f(i - 1) * i % MOD

    @lru_cache(None)
    def inv(self, i):
        return pow(i, MOD - 2, MOD)
