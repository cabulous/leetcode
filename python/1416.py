MOD = 10 ** 9 + 7


class Solution:

    def __init__(self):
        self.s = ''
        self.k = 0
        self.memo = {}

    def numberOfArrays(self, s: str, k: int) -> int:
        self.s = s
        self.k = k
        return self.dfs(0)

    def dfs(self, start_idx):
        if start_idx == len(self.s):
            return 1
        if self.s[start_idx] == '0':
            return 0
        if start_idx in self.memo:
            return self.memo[start_idx]

        num = 0
        res = 0
        for end_idx in range(start_idx, len(self.s)):
            num = num * 10 + int(self.s[end_idx])
            if num > self.k:
                break
            res += self.dfs(end_idx + 1)
            res %= MOD

        self.memo[start_idx] = res
        return res
