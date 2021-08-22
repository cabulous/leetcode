class Solution:
    def numDecodings(self, s: str) -> int:
        one = {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1}
        two = {'10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1, '16': 1, '17': 1, '18': 1, '19': 1, '20': 1,
               '21': 1, '22': 1, '23': 1, '24': 1, '25': 1, '26': 1}

        pre, cur = 1, one.get(s[0], 0)

        for i in range(1, len(s)):
            pre, cur = cur, one.get(s[i], 0) * cur + two.get(s[i - 1:i + 1], 0) * pre

        return cur


# recursive
class Solution:
    def __init__(self):
        self.memo = {}

    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        return self.helper(0, s)

    def helper(self, index, s):
        if index == len(s):
            return 1
        if s[index] == '0':
            return 0
        if index == len(s) - 1:
            return 1
        if index in self.memo:
            return self.memo[index]
        self.memo[index] = self.helper(index + 1, s) + (
            self.helper(index + 2, s) if int(s[index:index + 2]) <= 26 else 0)
        return self.memo[index]


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
