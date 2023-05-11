class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                dp[i][j] = max(
                    dp[i - 1][j - 1] + (nums1[i] == nums2[j]),
                    dp[i - 1][j],
                    dp[i][j - 1],
                )

        return dp[len(nums1) - 1][len(nums2) - 1]
