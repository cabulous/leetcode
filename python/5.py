# https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends).
class Solution:

    def __init__(self):
        self.s = ''

    def longestPalindrome(self, s: str) -> str:
        self.s = s
        res = ''

        for i in range(len(self.s)):
            res = max(self.helper(i, i), self.helper(i, i + 1), res, key=len)

        return res

    def helper(self, left, right):
        while 0 <= left and right < len(self.s) and self.s[left] == self.s[right]:
            left -= 1
            right += 1
        return self.s[left + 1:right]


# https://leetcode.com/problems/longest-palindromic-substring/discuss/121496/Python-DP-solution/194444
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        max_length = 0
        res = ''

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1] == 1):
                    dp[i][j] = 1
                    if res == '' or max_length < j - i + 1:
                        max_length = j - i + 1
                        res = s[i:j + 1]

        return res
