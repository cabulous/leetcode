from collections import defaultdict
from typing import List


# convert to longest common substring problem
# https://leetcode.com/problems/uncrossed-lines/discuss/282842/JavaC%2B%2BPython-DP-The-Longest-Common-Subsequence
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = defaultdict(int)

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                dp[i, j] = max(
                    dp[i - 1, j - 1] + (nums1[i] == nums2[j]),
                    dp[i - 1, j],
                    dp[i, j - 1],
                )

        return dp[len(nums1) - 1, len(nums2) - 1]
