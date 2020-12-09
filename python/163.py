class Solution:
    def findMissingRanges(self, nums, lower, upper):
        nums = [lower - 1] + nums + [upper + 1]
        res = []
        for i in range(len(nums) - 1):
            curr = nums[i]
            next = nums[i + 1]
            if next - curr == 2:
                res.append(str(curr + 1))
            elif next - curr > 2:
                res.append(str(curr + 1) + "->" + str(next - 1))
        return res
