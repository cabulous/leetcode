from typing import List


# https://leetcode.com/problems/array-nesting/discuss/102473/JavaC%2B%2BPython-Straight-Forward
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        seen = [0] * len(nums)
        res = 0

        for n in nums:
            cnt = 0
            while not seen[n]:
                seen[n] = 1
                cnt += 1
                n = nums[n]
            res = max(res, cnt)

        return res
