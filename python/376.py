from typing import List


# better dp
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        up = down = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
        return max(up, down)


# https://leetcode.com/problems/wiggle-subsequence/discuss/84921/3-lines-O(n)-Python-with-explanationproof
# because there are two 'nan' in the diffs,
# where 'nan' times anything equals to 'nan', and 'nan' >= 0 or 'nan' <= 0 are both False
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        nan = float('nan')
        diffs = [a - b for a, b in zip([nan] + nums, nums + [nan]) if a - b]
        return sum(not d * e >= 0 for d, e in zip(diffs, diffs[1:]))


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        trend = peak = 0
        for prev, curr in zip(nums, nums[1:]):
            if diff := curr - prev:
                if trend * diff < 0:
                    peak += 1
                trend = diff
        return peak + 2 if trend else int(bool(nums))


# dp
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return n

        up, down = [1] * n, [1] * n

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                down[i] = up[i - 1] + 1
                up[i] = up[i - 1]
            else:
                down[i] = down[i - 1]
                up[i] = up[i - 1]

        return max(down[-1], up[-1])
