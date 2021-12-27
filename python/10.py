class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))

        return first_match and self.isMatch(s[1:], p[1:])


class Solution:

    def __init__(self):
        self.memo = {}
        self.s = ''
        self.p = ''

    def isMatch(self, s: str, p: str) -> bool:
        self.s, self.p = s, p
        return self.dp(0, 0)

    def dp(self, i, j):
        if (i, j) in self.memo:
            return self.memo[i, j]

        if j == len(self.p):
            ans = i == len(self.s)
        else:
            first_match = i < len(self.s) and self.p[j] in {self.s[i], '.'}
            if j + 1 < len(self.p) and self.p[j + 1] == '*':
                ans = self.dp(i, j + 2) or (first_match and self.dp(i + 1, j))
            else:
                ans = first_match and self.dp(i + 1, j + 1)

        self.memo[i, j] = ans

        return ans
