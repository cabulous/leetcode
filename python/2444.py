class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        last_min_idx = -1
        last_max_idx = -1
        left = -1
        res = 0

        for idx, val in enumerate(nums):
            if minK <= val <= maxK:
                if val == minK:
                    last_min_idx = idx
                if val == maxK:
                    last_max_idx = idx
                res += max(0, min(last_min_idx, last_max_idx) - left)
            else:
                last_min_idx = -1
                last_max_idx = -1
                left = idx

        return res
