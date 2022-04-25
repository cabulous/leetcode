# https://leetcode.com/problems/encode-string-with-shortest-length/discuss/95602/Short-Python
class Solution:

    def __init__(self):
        self.memo = {}

    def encode(self, s: str) -> str:
        return self.helper(s)

    def helper(self, s):
        if s in self.memo:
            return self.memo[s]

        n = len(s)
        i = (s + s).find(s, 1)

        one = '%d[%s]' % (n // i, self.helper(s[:i])) if i < n else s
        multi = [self.helper(s[:i]) + self.helper(s[i:]) for i in range(1, n)]

        self.memo[s] = min([s, one] + multi, key=len)

        return self.memo[s]
