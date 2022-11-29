# https://leetcode.com/problems/valid-palindrome-iii/discuss/397634/Python3-Edit-Distance
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]

        for i in range(len(s) + 1):
            for j in range(len(s) + 1):
                if i == 0 or j == 0:
                    dp[i][j] = i or j
                elif s[i - 1] == s[len(s) - j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1] <= 2 * k
