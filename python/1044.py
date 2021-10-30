from functools import reduce


# https://leetcode.com/problems/longest-duplicate-substring/discuss/290871/Python-Binary-Search
class Solution:
    def __init__(self):
        self.MOD = 2 ** 63 - 1
        self.hashes = []
        self.s_length = 0

    def longestDupSubstring(self, s: str) -> str:
        self.s_length = len(s)
        self.hashes = [ord(c) - ord('a') for c in s]
        lo, hi = 0, self.s_length
        res = 0
        while lo < hi:
            mi = (lo + hi + 1) // 2
            pos = self.test(mi)
            if pos:
                lo = mi
                res = pos
            else:
                hi = mi - 1
        return s[res:res + lo]

    def test(self, length):
        p = pow(26, length, self.MOD)
        cur = reduce(lambda x, y: (x * 26 + y) % self.MOD, self.hashes[:length], 0)
        seen = {cur}
        for i in range(length, self.s_length):
            cur = (cur * 26 + self.hashes[i] - self.hashes[i - length] * p) % self.MOD
            if cur in seen:
                return i - length + 1
            seen.add(cur)
