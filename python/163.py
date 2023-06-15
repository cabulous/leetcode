class Solution:
    def findMissingRanges(self, nums, lower, upper):
        inclusive_nums = [lower - 1] + nums + [upper + 1]
        res = []

        for i in range(len(inclusive_nums) - 1):
            curr_num = inclusive_nums[i]
            next_num = inclusive_nums[i + 1]
            if next_num - curr_num >= 2:
                res.append([curr_num + 1, next_num - 1])

        return res
