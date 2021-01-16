# https://leetcode.com/problems/get-maximum-in-generated-array/discuss/1017760/Python-Simulate-process-explained
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0] * (n + 2)
        nums[1] = 1
        for i in range(2, n + 1):
            nums[i] = nums[i // 2] + nums[i // 2 + 1] * (i % 2)
        return max(nums[:n + 1])


# O(n/2)
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [0] * (n + 1)
        nums[1] = 1
        maxi = 1
        for i in range(1, n // 2 + 1):
            nums[i * 2] = nums[i]
            if i * 2 + 1 <= n:
                nums[i * 2 + 1] = nums[i] + nums[i + 1]
                maxi = max(maxi, nums[i * 2 + 1])
        return maxi
