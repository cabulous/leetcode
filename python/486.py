# https://leetcode.com/problems/predict-the-winner/solutions/3827565/simple-answer-beats-100-runtime-ms/
class Solution:
    def PredictTheWinner(self, nums: list[int]) -> bool:
        dp = nums[:]

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

        return dp[-1] >= 0
