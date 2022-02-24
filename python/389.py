from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        for i in range(len(sorted_s)):
            if sorted_s[i] != sorted_t[i]:
                return sorted_t[i]

        return sorted_t[-1]


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)

        for c in t:
            if c not in count_s or count_s[c] == 0:
                return c
            count_s[c] -= 1


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ch = 0

        for c in s:
            ch ^= ord(c)

        for c in t:
            ch ^= ord(c)

        return chr(ch)
