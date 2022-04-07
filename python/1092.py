# https://leetcode.com/problems/shortest-common-supersequence/discuss/312710/C%2B%2BPython-Find-the-LCS
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        i, j = 0, 0
        res = ''

        for ch in self.longest_common_string(str1, str2):
            while str1[i] != ch:
                res += str1[i]
                i += 1
            while str2[j] != ch:
                res += str2[j]
                j += 1
            res += ch
            i += 1
            j += 1

        return res + str1[i:] + str2[j:]

    def longest_common_string(self, str1, str2):
        str1_len = len(str1)
        str2_len = len(str2)
        dp = [[''] * (str2_len + 1) for _ in range(str1_len + 1)]

        for i in range(str1_len):
            for j in range(str2_len):
                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + str1[i]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)

        return dp[-1][-1]
