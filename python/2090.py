class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        res = [-1] * len(nums)

        curr = 0
        left = 0
        diameter = 2 * k + 1

        for right in range(len(nums)):
            curr += nums[right]
            if right - left + 1 >= diameter:
                res[left + k] = curr // diameter
                curr -= nums[left]
                left += 1

        return res
