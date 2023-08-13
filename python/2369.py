# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/solutions/3901261/100-o-n-dynamic-programming-sliding-window-video-optimal-solution/
class Solution:
    def validPartition(self, nums: list[int]) -> bool:
        if len(nums) <= 1:
            return False

        dp = [True, False, nums[0] == nums[1]]

        for i in range(2, len(nums)):
            curr = False
            if nums[i] == nums[i - 1] and dp[1]:
                curr = True
            elif nums[i] == nums[i - 1] == nums[i - 2] and dp[0]:
                curr = True
            elif nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2] == 1 and dp[0]:
                curr = True
            dp[0], dp[1], dp[2] = dp[1], dp[2], curr

        return dp[-1]
