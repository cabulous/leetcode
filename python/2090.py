class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        res = [-1] * len(nums)

        left = 0
        curr = 0
        win_size = 2 * k + 1

        for right in range(len(nums)):
            curr += nums[right]
            if right - left + 1 == win_size:
                res[left + k] = curr // win_size
                curr -= nums[left]
                left += 1

        return res
