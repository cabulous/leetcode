# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/solutions/3840553/100-dp-video-decoding-approach-to-minimum-ascii-delete-sum/
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        if len(s1) > len(s2):
            s1, s2 = s2, s1

        dp = [0] * (len(s2) + 1)
        for j in range(1, len(s2) + 1):
            dp[j] = dp[j - 1] + ord(s2[j - 1])

        for i in range(1, len(s1) + 1):
            next_dp = [dp[0] + ord(s1[i - 1])]
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    next_dp.append(dp[j - 1])
                else:
                    next_dp.append(min(
                        dp[j] + ord(s1[i - 1]),
                        next_dp[j - 1] + ord(s2[j - 1]),
                    ))
            dp = next_dp

        return dp[-1]
