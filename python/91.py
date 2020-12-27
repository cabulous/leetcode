# recursive
class Solution:
    def __init__(self):
        self.memo = {}

    def helper(self, index, s):
        if index == len(s):
            return 1
        if s[index] == '0':
            return 0
        if index == len(s) - 1:
            return 1
        if index in self.memo:
            return self.memo[index]
        ans = self.helper(index + 1, s) + (self.helper(index + 2, s) if (int(s[index:index + 2]) <= 26) else 0)
        self.memo[index] = ans
        return ans

    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        return self.helper(0, s)


# dp
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, n + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]
