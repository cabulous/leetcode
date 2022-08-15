import re


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        pattern = re.compile(r'^(.+)\1+$')
        return pattern.match(s) is not None


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        dp = [0] * len(s)

        for i in range(1, len(s)):
            j = dp[i - 1]
            while j > 0 and s[i] != s[j]:
                j = dp[j - 1]
            if s[i] == s[j]:
                j += 1
            dp[i] = j

        res = dp[-1]

        return res != 0 and len(s) % (len(s) - res) == 0
