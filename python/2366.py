# https://leetcode.com/problems/minimum-replacements-to-sort-the-array/solutions/3978548/easy-to-understand-full-explanation-done-in-few-steps-o-n-solution/
class Solution:
    def minimumReplacement(self, nums: list[int]) -> int:
        last = nums[-1]
        res = 0

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= last:
                last = nums[i]
            else:
                buckets = nums[i] // last
                if nums[i] % last > 0:
                    buckets += 1
                last = nums[i] // buckets
                res += buckets - 1

        return res
