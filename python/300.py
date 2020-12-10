# DP
class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        m = len(nums)
        dp = [0] * m
        dp[0] = 1
        ans = 1
        for i in range(1, m):
            cur_max = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    cur_max = max(cur_max, dp[j])
            dp[i] = cur_max + 1
            ans = max(ans, dp[i])
        return ans


# DP - binary
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        tails = [0] * len(nums)
        size = 0
        for n in nums:
            left = 0
            right = size
            while left < right:
                mid = left + (right - left) // 2
                if tails[mid] < n:
                    left = mid + 1
                else:
                    right = mid
            tails[left] = n
            if left == size:
                size += 1
        return size
