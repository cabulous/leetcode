# https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends).
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def helper(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        res = ""
        for i in range(n):
            res = max(helper(i, i), helper(i, i + 1), res, key=len)
        return res


# dp
# https://leetcode.com/problems/longest-palindromic-substring/discuss/121496/Python-DP-solution/194444
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        res = ""
        maxi = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1] == 1):
                    dp[i][j] = 1
                    if res == "" or maxi < j - i + 1:
                        maxi = j - i + 1
                        res = s[i:j + 1]
        return res
