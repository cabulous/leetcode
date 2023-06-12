# https://leetcode.com/problems/summary-ranges/discuss/63193/6-lines-in-Python
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []

        ranges = []
        curr_range = [nums[0]]

        for num in nums[1:]:
            if num - 1 not in curr_range:
                ranges.append(curr_range[:])
                curr_range = []
            curr_range[1:] = [num]

        if curr_range:
            ranges.append(curr_range[:])

        return ['->'.join(map(str, r)) for r in ranges]
