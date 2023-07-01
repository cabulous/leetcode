# https://leetcode.com/problems/fair-distribution-of-cookies/solutions/3702322/w-explanation-c-python-with-recursive-dp-bitmask/
class Solution:

    def __init__(self):
        self.cookies = []
        self.dp = []

    def distributeCookies(self, cookies: list[int], k: int) -> int:
        self.cookies = cookies
        self.dp = [[-1] * (1 << len(cookies)) for _ in range(k + 1)]
        return self.unfairness(k, (1 << len(cookies)) - 1)

    def unfairness(self, k, mask):
        if self.dp[k][mask] != -1:
            return self.dp[k][mask]

        if k == 1:
            self.dp[k][mask] = self.sum_cookies(mask)
            return self.dp[k][mask]

        res = 2 ** 31
        curr_mask = mask
        while curr_mask > 0:
            sum1 = self.sum_cookies(curr_mask)
            sum2 = self.unfairness(k - 1, curr_mask ^ mask)
            res = min(res, max(sum1, sum2))
            curr_mask = (curr_mask - 1) & mask

        self.dp[k][mask] = res

        return res

    def sum_cookies(self, mask):
        res = 0
        for i in range(len(self.cookies)):
            if mask & (1 << i):
                res += self.cookies[i]
        return res
