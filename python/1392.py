MOD = 10 ** 9 + 7


# https://leetcode.com/problems/longest-happy-prefix/discuss/547237/JavaPython-Rolling-Hash
class Solution:
    def longestPrefix(self, s: str) -> str:
        prefix_hash, suffix_hash = 0, 0
        res = 0

        for i in range(len(s) - 1):
            prefix_hash = (prefix_hash * 128 + ord(s[i])) % MOD
            suffix_hash = (suffix_hash + pow(128, i, MOD) * ord(s[~i])) % MOD
            if prefix_hash == suffix_hash:
                res = i + 1

        return s[:res]


class Solution:
    def longestPrefix(self, s: str) -> str:
        i = len(s) - 1
        while i > 0:
            if s[:i] == s[-i:]:
                return s[:i]
            i -= 1
        return ''
