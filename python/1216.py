# https://leetcode.com/problems/valid-palindrome-iii/discuss/397634/Python3-Edit-Distance
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]

        for start in range(len(s) + 1):
            for end in range(len(s) + 1):
                if start == 0 or end == 0:
                    dp[start][end] = start or end
                elif s[start - 1] == s[len(s) - end]:
                    dp[start][end] = dp[start - 1][end - 1]
                else:
                    dp[start][end] = 1 + min(dp[start - 1][end], dp[start][end - 1])

        return dp[-1][-1] <= 2 * k
