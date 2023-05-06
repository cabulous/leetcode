MOD = 10 ** 9 + 7


class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        sorted_nums = sorted(nums)

        left = 0
        right = len(sorted_nums) - 1
        res = 0

        while left <= right:
            if sorted_nums[left] + sorted_nums[right] <= target:
                res += pow(2, right - left, MOD)
                left += 1
            else:
                right -= 1

        return res % MOD
