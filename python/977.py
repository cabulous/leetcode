class Solution:
    def sortedSquares(self, nums: [int]) -> [int]:
        n = len(nums)
        j = 0
        while j < n and nums[j] < 0:
            j += 1
        i = j - 1

        ans = []
        while i >= 0 and j < n:
            if nums[i] ** 2 < nums[j] ** 2:
                ans.append(nums[i] ** 2)
                i -= 1
            else:
                ans.append(nums[j] ** 2)
                j += 1

        while i >= 0:
            ans.append(nums[i] ** 2)
            i -= 1
        while j < n:
            ans.append(nums[j] ** 2)
            j += 1

        return ans
