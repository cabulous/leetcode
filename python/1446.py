class Solution:
    def maxPower(self, s: str) -> int:
        res = total = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                total += 1
            else:
                total = 1
            res = max(res, total)

        return res
